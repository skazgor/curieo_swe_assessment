from transaction import TransactionType, Transaction, Transactions
from query import Query

import sys
import threading

input_file = sys.argv[1]

with open(input_file, 'r') as file:
    initial_params = file.readline().strip().split()
    initial_balance = int(initial_params[0])
    num_transactions = int(initial_params[1])
    num_queries = int(initial_params[2])

    transactions = Transactions(initial_balance)

    for i in range(num_transactions):
        params = file.readline().strip().split()
        time_stamp = int(params[0])
        if params[1] == 'Deposit':
            transaction_type = TransactionType.DEPOSIT
        elif params[1] == 'Withdraw':
            transaction_type = TransactionType.WITHDRAW
        
        amount = int(params[2])
        transaction = Transaction(amount, time_stamp, transaction_type)
        transactions.add_transaction(transaction)
    
    transactions.set_initial_feasible_withdrawal()

    transactions.print_transactions()

    query = Query()
    end_index = len(transactions.transactions) - 1
    for i in range(num_queries):
        params = file.readline().strip().split()
        start_time = int(params[1])
        end_time = int(params[2])

        threading.Thread(target=query.query, args=(transactions.transactions, start_time, end_time, end_index)).start()
        # query.query(transactions.transactions, start_time, end_time, end_index)