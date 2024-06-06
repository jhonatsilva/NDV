import requests
from datetime import datetime

transactions_log = []
validations = []

def validate_transaction_util(data):
    transaction = data['transaction']
    key = data['key']

    # Simular a validação da transação
    current_time = datetime.now().isoformat()
    validation = {
        'transaction': transaction,
        'key': key,
        'status': 1,  # Sucesso
        'timestamp': current_time
    }
    validations.append(validation)

    # Enviar resultado para o seletor
    requests.post(f'http://localhost:5001/seletor/validation_result', json={'validation': validation})
    
    return {'status': 1, 'message': 'Transação validada com sucesso'}, 200
