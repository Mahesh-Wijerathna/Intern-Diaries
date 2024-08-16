from functools import wraps
from flask import request, jsonify
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].replace('Bearer ', '')
        if not token:
            return jsonify({'error': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, 'secretkey', algorithms=["HS256"])
            current_user = {'username': data['username']}
        except:
            return jsonify({'error': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
