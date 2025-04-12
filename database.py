import sqlite3
import logging
from config import DATABASE_FILE

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db():
    """Initialize the database if it doesn't exist."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    # Create users table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        has_invited_friend INTEGER DEFAULT 0
    )
    ''')
    
    # Create referrals table to track invitations
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS referrals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        referrer_id INTEGER,
        referred_id INTEGER,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (referrer_id) REFERENCES users(user_id),
        FOREIGN KEY (referred_id) REFERENCES users(user_id)
    )
    ''')
    
    conn.commit()
    conn.close()
    logger.info("Database initialized successfully")

def add_user(user_id, username=None, first_name=None, last_name=None, has_invited=0):
    """Add a new user to the database or update existing user."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    try:
        # Check if user already exists
        cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (user_id,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            # Update existing user but don't change has_invited_friend status
            cursor.execute('''
            UPDATE users 
            SET username = ?, first_name = ?, last_name = ?
            WHERE user_id = ?
            ''', (username, first_name, last_name, user_id))
        else:
            # Insert new user with has_invited_friend status
            cursor.execute('''
            INSERT INTO users (user_id, username, first_name, last_name, has_invited_friend)
            VALUES (?, ?, ?, ?, ?)
            ''', (user_id, username, first_name, last_name, has_invited))
        
        conn.commit()
        logger.info(f"User {user_id} added/updated in database")
    except Exception as e:
        logger.error(f"Error adding user to database: {e}")
    finally:
        conn.close()

def get_user(user_id):
    """Get user information from the database."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    
    conn.close()
    return user

def get_all_users():
    """Get all users from the database."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute('SELECT user_id FROM users')
    users = [row[0] for row in cursor.fetchall()]
    
    conn.close()
    return users

def remove_user(user_id):
    """Remove a user from the database."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
    
    conn.commit()
    conn.close()
    logger.info(f"User {user_id} removed from database")

def add_referral(referrer_id, referred_id):
    """Add a new referral record."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    try:
        # Add the referral record
        cursor.execute('''
        INSERT INTO referrals (referrer_id, referred_id)
        VALUES (?, ?)
        ''', (referrer_id, referred_id))
        
        # Update referrer's has_invited_friend status
        cursor.execute('''
        UPDATE users
        SET has_invited_friend = 1
        WHERE user_id = ?
        ''', (referrer_id,))
        
        conn.commit()
        logger.info(f"User {referred_id} was referred by {referrer_id}")
        return True
    except Exception as e:
        logger.error(f"Error adding referral: {e}")
        return False
    finally:
        conn.close()

def has_invited_friend(user_id):
    """Check if user has invited at least one friend."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    # Check if user has the has_invited_friend flag set
    cursor.execute('SELECT has_invited_friend FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    
    # Also check the referrals table directly
    cursor.execute('SELECT COUNT(*) FROM referrals WHERE referrer_id = ?', (user_id,))
    referral_count = cursor.fetchone()[0]
    
    conn.close()
    
    # Return True if either condition is met
    if result and result[0] == 1:
        return True
    if referral_count > 0:
        return True
    return False

def get_referrer(user_id):
    """Get the referrer of a user, if any."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute('SELECT referrer_id FROM referrals WHERE referred_id = ?', (user_id,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return result[0]
    return None
