import os
import json
import sqlite3
import datetime
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "masterquiz_stats_secret")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Configure the database using bot's SQLite database directly for read-only access
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///../bot_users.db")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
db.init_app(app)

# Import models
from models import User, Referral


# Main route for the dashboard
@app.route('/')
def index():
    return render_template('index.html')


# API endpoint to get basic statistics
@app.route('/api/stats', methods=['GET'])
def get_stats():
    # Get total users count
    users_count = User.query.count()
    
    # Get active users (users who have interacted with the bot in the last 7 days)
    # Note: Since we don't have a 'last_activity' field, this will be all users
    active_users = users_count
    
    # Get total referrals
    referrals_count = Referral.query.count()
    
    # Get user registration over time (by day)
    # Note: Since we don't store registration date, we can't provide this data
    # We'll just return empty data for this
    
    # Load test data from json file
    tests_count = 0
    try:
        with open('../user_tests.json', 'r', encoding='utf-8') as f:
            tests_data = json.load(f)
            # Count all tests across users
            for user_id, tests in tests_data.items():
                tests_count += len(tests)
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or is invalid, just use 0
        pass
    
    # Return statistics
    return jsonify({
        'total_users': users_count,
        'active_users': active_users,
        'total_referrals': referrals_count,
        'total_tests': tests_count,
        'updated_at': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })


# API endpoint to get user data
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_data = [{
        'id': user.id,
        'username': user.username or 'No Username',
        'first_name': user.first_name or 'Unknown',
        'last_name': user.last_name or '',
        'has_invited': user.has_invited,
    } for user in users]
    
    return jsonify(user_data)


# API endpoint to get test data
@app.route('/api/tests', methods=['GET'])
def get_tests():
    tests_by_user = {}
    
    try:
        with open('../user_tests.json', 'r', encoding='utf-8') as f:
            tests_data = json.load(f)
            
            for user_id, tests in tests_data.items():
                # Convert user_id to integer
                user_id_int = int(user_id)
                
                # Get user info
                user = User.query.get(user_id_int)
                if not user:
                    username = "Unknown User"
                    full_name = "Unknown"
                else:
                    username = user.username or "No Username"
                    full_name = f"{user.first_name or ''} {user.last_name or ''}".strip() or "Unknown"
                
                # Count tests and questions
                test_count = len(tests)
                total_questions = sum(len(test.get('questions', [])) for test in tests)
                
                tests_by_user[user_id] = {
                    'user_id': user_id_int,
                    'username': username,
                    'full_name': full_name,
                    'test_count': test_count,
                    'total_questions': total_questions,
                    'tests': [{
                        'name': test.get('name', 'Unnamed Test'),
                        'questions_count': len(test.get('questions', [])),
                    } for test in tests]
                }
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or is invalid, return empty data
        pass
    
    return jsonify(list(tests_by_user.values()))


# API endpoint to get referral data
@app.route('/api/referrals', methods=['GET'])
def get_referrals():
    referrals = Referral.query.all()
    
    referral_data = []
    for ref in referrals:
        referrer = User.query.get(ref.referrer_id)
        referred = User.query.get(ref.referred_id)
        
        referral_data.append({
            'id': ref.id,
            'referrer_id': ref.referrer_id,
            'referrer_username': referrer.username if referrer else 'Unknown',
            'referrer_name': f"{referrer.first_name or ''} {referrer.last_name or ''}".strip() if referrer else 'Unknown',
            'referred_id': ref.referred_id,
            'referred_username': referred.username if referred else 'Unknown',
            'referred_name': f"{referred.first_name or ''} {referred.last_name or ''}".strip() if referred else 'Unknown',
        })
    
    return jsonify(referral_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)