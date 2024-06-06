from datetime import datetime

accounts = {}
transactions = []

def create_account_util(data):
    account_id = data['account_id']
    balance = data['balance']

    if account_id in accounts:
        return {'status': 2, 'message': 'Conta já existe'}, 400

    accounts[account_id] = balance
    return {'status': 1, 'message': 'Conta criada com sucesso'}, 201

def create_transaction_util(data):
    sender = data['sender']
    receiver = data['receiver']
    amount = data['amount']
    fee = data['fee']
    timestamp = datetime.now()

    if accounts.get(sender, 0) < amount + fee:
        return {'status': 2, 'message': 'Saldo insuficiente'}, 400

    transactions.append({
        'sender': sender,
        'receiver': receiver,
        'amount': amount,
        'fee': fee,
        'timestamp': timestamp
    })
    
    return {'status': 1, 'message': 'Transação criada com sucesso'}, 201

def get_current_time():
    return datetime.now().isoformat()
