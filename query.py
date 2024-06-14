from transaction import TransactionType


class Query:

    def query(self, transactions, start_time, end_time, end_index):

        start_index = self.get_start_index(transactions, start_time, end_index)
        end_index = self.get_end_index(transactions, end_time, end_index)

        previous_withdrawals = self.calculate_previous_withdrawals(transactions, start_index, end_index)

        deposits = []
        withdrawals = []
        for i in range(start_index, end_index+1):
            if transactions[i].transaction_type == TransactionType.DEPOSIT:
                deposits.append(transactions[i])
            else:
                withdrawals.append(transactions[i])
        
        dp = [[(0, 0) for _ in range(len(withdrawals) + 1)] for _ in range(len(deposits) + 1)]

        dp[0][0] = (0, transactions[start_index].balance)
        
        for i in range(1, len(deposits)+1):
            _, previous_balance = dp[i-1][0]
            dp[i][0] = (0, previous_balance + deposits[i-1].amount)

        for i in range(0, len(deposits)+1):
            for j in range(1, len(withdrawals)+1):

                if i == 0:
                    dp[i][j] = dp[i][j-1]
                    if dp[i][j][1] >= withdrawals[j-1].amount:
                        dp[i][j] = (dp[i][j][0] + 1, dp[i][j][1] - withdrawals[j-1].amount)
                    continue

                i_withdrawals, i_balance = dp[i-1][j]
                j_withdrawals, j_balance = dp[i][j-1]

                if j_balance >= withdrawals[j-1].amount:
                    j_withdrawals += 1
                    j_balance -= withdrawals[j-1].amount
                
                i_balance += deposits[i-1].amount

                if j_withdrawals > i_withdrawals:
                    dp[i][j] = (j_withdrawals, j_balance)
                elif j_withdrawals < i_withdrawals:
                    dp[i][j] = (i_withdrawals, i_balance)
                else:
                    dp[i][j] = (i_withdrawals, max(i_balance, j_balance))

        print(f"Query {start_time} {end_time} : " + str(dp[len(deposits)][len(withdrawals)][0] - previous_withdrawals))
                    
    
    def get_start_index(self, transactions, start_time, end_index):
        start = 0
        end = end_index
        while start < end:
            mid = (start + end) // 2
            if transactions[mid].time_stamp < start_time:
                start = mid + 1
            else:
                end = mid
        
        return start
    
    def get_end_index(self, transactions, end_time, end_index):
        start = 0
        end = end_index
        while start < end:
            mid = (start + end) // 2 
                
            if transactions[mid].time_stamp > end_time:
                end = mid-1
            else:
                start = mid
            
            if start == mid:
                if transactions[end].time_stamp <= end_time:
                    return end
                else:
                    return start
        return end
    
    def calculate_previous_withdrawals(self, transactions, start_index, end_index):
        previous_withdrawals_excluding_start = transactions[end_index].successful_withdrawals - transactions[start_index].successful_withdrawals

        if transactions[start_index].transaction_type == TransactionType.WITHDRAW and transactions[start_index].can_withdraw:
            previous_withdrawals_including_start = previous_withdrawals_excluding_start + 1
        else:
            previous_withdrawals_including_start = previous_withdrawals_excluding_start
        
        return previous_withdrawals_including_start
