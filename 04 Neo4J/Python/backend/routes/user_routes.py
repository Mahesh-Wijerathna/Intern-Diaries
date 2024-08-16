from flask import Blueprint
from controllers.user_controller import update_password, delete_account

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/update-password', methods=['PUT'])(update_password)
user_bp.route('/delete-account', methods=['DELETE'])(delete_account)
