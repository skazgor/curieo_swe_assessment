from transaction import TransactionType


class Query:

    def query(self, transactions, start_time, end_time, end_index):

        start_index = self.get_start_index(transactions, start_time, end_index)
        end_index = self.get_end_index(transactions, end_time, end_index)

        total_balance =  transactions[end_index].cumulative_sum_including_current - transactions[start_index].cumulative_sum + transactions[start_index].balance

        new_withdrawal = 0

        for i in range(start_index, end_index+1):
            if transactions[i].transaction_type == TransactionType.WITHDRAW:
                total_balance -= transactions[i].amount
                if total_balance >= 0 and not transactions[i].can_withdraw:
                    new_withdrawal += 1
        
        print(new_withdrawal)
                    
    
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

