from flask import request, jsonify
from models.user_model import User
from middleware.auth_middleware import token_required

@token_required
def update_password(current_user):
    data = request.get_json()
    new_password = data['new_password']
    
    try:
        User.update_password(current_user['username'], generate_password_hash(new_password, method='sha256'))
        return jsonify({'message': 'Password updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@token_required
def delete_account(current_user):
    try:
        User.delete(current_user['username'])
        return jsonify({'message': 'Account deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
