import random
import requests

validators = {}
validator_keys = {}
active_transactions = []

def register_validator_util(data):
    validator_id = data['validator_id']
    stake = data['stake']

    if validator_id in validators:
        return {'status': 2, 'message': 'Validador já registrado'}, 400

    unique_key = f"key_{random.randint(1000, 9999)}"
    validators[validator_id] = {'stake': stake, 'key': unique_key, 'flag': 0}
    validator_keys[validator_id] = unique_key

    return {'status': 1, 'key': unique_key}, 201

def choose_validators_util(data):
    transaction = data['transaction']

    available_validators = [v for v in validators if validators[v]['flag'] < 2]
    if len(available_validators) < 3:
        return {'status': 2, 'message': 'Não há validadores suficientes'}, 400

    chosen_validators = random.sample(available_validators, 3)
    active_transactions.append({'transaction': transaction, 'validators': chosen_validators})
    
    # Enviar transação para os validadores
    for validator in chosen_validators:
        validator_key = validator_keys[validator]
        requests.post(f'http://localhost:5002/validador/validate', json={'transaction': transaction, 'key': validator_key})
    
    return {'status': 1, 'validators': chosen_validators}, 200
