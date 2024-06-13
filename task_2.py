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
    query = Query()

    for i in range(num_transactions + num_queries):
        params = file.readline().strip().split()

        if params[0] == 'Query':
            start_time = int(params[1])
            end_time = int(params[2])
            threading.Thread(target=query.query, args=(transactions.transactions, start_time, end_time, len(transactions.transactions) - 1)).start()
        else:
            time_stamp = int(params[0])
            if params[1] == 'Deposit':
                transaction_type = TransactionType.DEPOSIT
            elif params[1] == 'Withdraw':
                transaction_type = TransactionType.WITHDRAW
            
            amount = int(params[2])
            transaction = Transaction(amount, time_stamp, transaction_type)
            transactions.add_transaction_in_order(transaction)