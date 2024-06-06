from flask import Blueprint, request, jsonify
from datetime import datetime
from .utils import create_account_util, create_transaction_util, get_current_time

banco_bp = Blueprint('banco', __name__)

@banco_bp.route('/')
def home():
    return "Banco Service"

@banco_bp.route('/trans', methods=['POST'])
def create_transaction():
    data = request.get_json()
    response, status = create_transaction_util(data)
    return jsonify(response), status

@banco_bp.route('/accounts', methods=['POST'])
def create_account():
    data = request.get_json()
    response, status = create_account_util(data)
    return jsonify(response), status

@banco_bp.route('/hora', methods=['GET'])
def get_time():
    return jsonify({'time': get_current_time()}), 200
