from flask import Blueprint, request, jsonify
from .utils import validate_transaction_util

validador_bp = Blueprint('validador', __name__)

@validador_bp.route('/')
def home():
    return "Validador Service"

@validador_bp.route('/validador/validate', methods=['POST'])
def validate_transaction():
    data = request.get_json()
    response, status = validate_transaction_util(data)
    return jsonify(response), status
