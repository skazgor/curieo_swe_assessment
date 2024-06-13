from enum import Enum

class TransactionType(Enum):
    WITHDRAW = "Withdraw"
    DEPOSIT = "Deposit"


class Transaction:
    def __init__(self, amount, time_stamp, transaction_type):
        self.amount = amount
        self.time_stamp = time_stamp
        self.transaction_type = transaction_type

        # to calculate the balance
        self.balance = 0
        self.cumulative_sum = 0
        self.cumulative_sum_including_current = 0

        # for withdrawal transactions
        self.can_withdraw = False
    

    def __ge__(self, __value: object) -> bool:
        return self.time_stamp >= __value.time_stamp 

    def __lt__(self, __value: object) -> bool:
        return self.time_stamp < __value.time_stamp  
    
    def __str__(self) -> str:
        return f"{self.amount} {self.time_stamp} {self.transaction_type} {self.balance} {self.cumulative_sum} {self.cumulative_sum_including_current} {self.can_withdraw}"

class Transactions:
    def __init__(self, initial_balance):
        self.transactions = []
        self.initial_balance = initial_balance
        
        self.balance = initial_balance
        self.cumulative_sum = 0
        
    
    def add_transaction(self, transaction):
        self.transactions.append(transaction)
    
    def add_transaction_in_order(self, transaction):
        self.transactions.append(transaction)
        
        transaction.balance = self.balance
        transaction.cumulative_sum = self.cumulative_sum

        if transaction.transaction_type == TransactionType.DEPOSIT:
            self.cumulative_sum += transaction.amount
            self.balance += transaction.amount
            transaction.can_withdraw = True
        
        elif transaction.transaction_type == TransactionType.WITHDRAW:
            if self.balance >= transaction.amount:
                transaction.can_withdraw = True
                self.balance -= transaction.amount
        
        transaction.cumulative_sum_including_current = self.cumulative_sum
        
    
    def sort(self):
        return sorted(self.transactions)
    
    def set_initial_feasible_withdrawal(self):
        
        self.transactions = self.sort()

        balance = self.initial_balance
        cumulative_sum = 0

        for transaction in self.transactions:

            transaction.balance = balance
            transaction.cumulative_sum = cumulative_sum

            if transaction.transaction_type == TransactionType.DEPOSIT:
                cumulative_sum += transaction.amount
                balance += transaction.amount
                transaction.can_withdraw = True
            
            elif transaction.transaction_type == TransactionType.WITHDRAW:
                if balance >= transaction.amount:
                    transaction.can_withdraw = True
                    balance -= transaction.amount
            
            transaction.cumulative_sum_including_current = cumulative_sum
        
        self.balance = balance
        self.cumulative_sum = cumulative_sum
    def print_transactions(self):
        for transaction in self.transactions:
            print(transaction)
                
            
            
    

    
    