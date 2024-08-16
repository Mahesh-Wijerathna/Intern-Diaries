from flask import request, jsonify
from models.user_model import User
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

def signup():
    data = request.get_json()
    username = data['username']
    password = generate_password_hash(data['password'], method='sha256')
    try:
        User.create(username, password)
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def login():
    print('login')
    data = request.get_json()
    print(data)
    username = data['username']
    password = data['password']
    print("username: ", username)
    print("password: ", password)
    
    user_record = User.find_by_username(username)
    if not user_record:
        return jsonify({'error': 'User not found'}), 404
    
    if check_password_hash(user_record['password'], password):
        token = jwt.encode({'username': user_record['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, 'secretkey')
        return jsonify({'message': 'Login successful', 'token': token})
    else:
        return jsonify({'error': 'Invalid password'}), 400
