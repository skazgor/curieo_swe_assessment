import sys
import random


input_file = sys.argv[1]

initial_amount = int(sys.argv[2])

num_transactions = int(sys.argv[3])

num_queries = int(sys.argv[4])

task = int (sys.argv[5])


with open(input_file, 'w') as file:
    file.write(f"{initial_amount} {num_transactions} {num_queries}\n")

    if task == 1:
        for i in range(num_transactions):
            transaction_type = random.choice(["Deposit", "Withdraw"])
            amount = random.randint(1, 1000)
            file.write(f"{i} {transaction_type} {amount}\n")
        for i in range(num_queries):
            start_time = random.randint(0, num_transactions - 1)
            end_time = random.randint(start_time, num_transactions - 1)
            file.write(f"Query {start_time} {end_time}\n")
    else:
        i = 0
        j = 0
        while i < num_transactions or j < num_queries:
            if random.choice([True, False]) and i < num_transactions:
                transaction_type = random.choice(["Deposit", "Withdraw"])
                amount = random.randint(1, 1000)
                file.write(f"{i} {transaction_type} {amount}\n")
                i += 1
            elif j < num_queries:
                start_time = random.randint(0, num_transactions - 1)
                end_time = random.randint(start_time, num_transactions - 1)
                file.write(f"Query {start_time} {end_time}\n")
                j += 1 
        