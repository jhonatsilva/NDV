from flask import Blueprint, request, jsonify
import requests
from .utils import register_validator_util, choose_validators_util

seletor_bp = Blueprint('seletor', __name__)

@seletor_bp.route('/')
def home():
    return "Seletor Service"

@seletor_bp.route('/seletor/register', methods=['POST'])
def register_validator():
    data = request.get_json()
    response, status = register_validator_util(data)
    return jsonify(response), status

@seletor_bp.route('/seletor/choose', methods=['POST'])
def choose_validators():
    data = request.get_json()
    response, status = choose_validators_util(data)
    return jsonify(response), status
