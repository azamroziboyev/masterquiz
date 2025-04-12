from flask import Flask, jsonify
from app import app

def handler(event, context):
    """Netlify function handler"""
    return {
        "statusCode": 200,
        "body": "API is running"
    }