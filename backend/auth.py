from flask import Blueprint, request, jsonify, current_app
from models import create_user, verify_user
import jwt
import datetime

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400
        
    if create_user(username, password):
        return jsonify({'message': 'User registered successfully'}), 201
    else:
        return jsonify({'error': 'Username already exists'}), 409

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = verify_user(username, password)
    if user:
        token = jwt.encode({
            'user': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, current_app.config['SECRET_KEY'], algorithm="HS256")
        
        return jsonify({'token': token, 'username': username}), 200
    
    return jsonify({'error': 'Invalid credentials'}), 401
