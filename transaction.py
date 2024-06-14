from enum import Enum

class TransactionType(Enum):
    WITHDRAW = "Withdraw"
    DEPOSIT = "Deposit"


class Transaction:
    def __init__(self, amount, time_stamp, transaction_type):
        self.amount = amount
        self.time_stamp = time_stamp
        self.transaction_type = transaction_type

        # balance before the transaction
        self.balance = 0

        # for withdrawal transactions
        self.can_withdraw = False

        # total number of withdrawals successful including the current transaction
        self.successful_withdrawals = 0
    

    def __ge__(self, __value: object) -> bool:
        return self.time_stamp >= __value.time_stamp 

    def __lt__(self, __value: object) -> bool:
        return self.time_stamp < __value.time_stamp  
    
    def __str__(self) -> str:
        return f"{self.amount} {self.time_stamp} {self.transaction_type} {self.balance} {self.can_withdraw}"

class Transactions:
    def __init__(self, initial_balance):
        self.transactions = []
        self.initial_balance = initial_balance
        
        self.balance = initial_balance
        self.successful_withdrawals = 0
        
    
    def add_transaction(self, transaction):
        self.transactions.append(transaction)
    
    def add_transaction_in_order(self, transaction):
        self.transactions.append(transaction)
        
        transaction.balance = self.balance

        if transaction.transaction_type == TransactionType.DEPOSIT:
            self.balance += transaction.amount
            transaction.can_withdraw = True
        
        elif transaction.transaction_type == TransactionType.WITHDRAW:
            if self.balance >= transaction.amount:
                transaction.can_withdraw = True
                self.balance -= transaction.amount
                self.successful_withdrawals += 1
        
        transaction.successful_withdrawals = self.successful_withdrawals
               
    
    def sort(self):
        return sorted(self.transactions)
    
    def set_initial_feasible_withdrawal(self):
        
        self.transactions = self.sort()

        balance = self.initial_balance

        for transaction in self.transactions:

            transaction.balance = balance

            if transaction.transaction_type == TransactionType.DEPOSIT:
                balance += transaction.amount
                transaction.can_withdraw = True
            
            elif transaction.transaction_type == TransactionType.WITHDRAW:
                if balance >= transaction.amount:
                    transaction.can_withdraw = True
                    balance -= transaction.amount
                    self.successful_withdrawals += 1
            
            transaction.successful_withdrawals = self.successful_withdrawals
            
        self.balance = balance
        
    def print_transactions(self):
        for transaction in self.transactions:
            print(transaction)
                
            
            
    

    
    