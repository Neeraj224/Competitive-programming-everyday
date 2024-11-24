"""
    This question was part of the ServiceNow AMS Coding Challenge 2024,
    that was hella easy, but somehow I did not try to implement for some stupid
    reason.
    
    (-.-)
    
    Now that I did it, it makes sense that it takes a bit of time to understand the 
    order of checks for transactions.
    
    All in all, fun.
    Need to practice waaaaayyyyy more though, so that I complete things in the time given.
"""

class Solution:
    def __init__(self):
        self.customerDetails = []
        self.ledger = set()
        self.BUDGET_INDEX = 1
        self.PIN_INDEX = 2
        self.DAILY_TRANSACTIONS_INDEX = 3
        self.DAILY_LIMIT = 10
        self.TRANSACTION_LIMIT = 50000
            
    def solver(self, customerBudget, transactions):
        # pass
        for i in range(len(customerBudget)):
            # building our customer structure:
            # 0 -> id, 
            # 1 -> budget, 
            # 2 -> pin
            # 3 -> total daily transactions
            self.customerDetails.append([i + 1, customerBudget[i], -1, 0])
        
        for i in range(len(transactions)):
            # adding first-found PINs
            if self.customerDetails[transactions[i][0] - 1][2] == -1:
                self.customerDetails[transactions[i][0] - 1][2] = transactions[i][2]
        
        print("Initial Details: " + str(self.customerDetails))
        checks = []
        
        for customerID, amount, pin in transactions:
            # print(customerID)
            # print(self.customerDetails[customerID - 1])
            
            # first we check if we've already seen this transaction or not
            # (i.e. if its in the ledger or not):
            if (customerID, amount, pin) in self.ledger:
                checks.append("DUPLICATE")
                continue
            
            # if the customer has already placed 10 orders that day i.e.,
            # that is the customer has reached the daily limit of orders
            if self.customerDetails[customerID - 1][self.DAILY_TRANSACTIONS_INDEX] >= self.DAILY_LIMIT:
                checks.append("INVALID")
                continue
            
            # if the customer is trying to place an order of more than the
            # one-time transaction limit:
            if amount > self.TRANSACTION_LIMIT:
                checks.append("INVALID")
                continue
            
            # if the customer entered the wrong PIN:
            if self.customerDetails[customerID - 1][self.PIN_INDEX] != pin:
                checks.append("INVALID")
                continue
            
            # if the amount of the transaction is more than the
            # the customer's remaining budget:
            if amount > self.customerDetails[customerID - 1][self.BUDGET_INDEX]:
                checks.append("INVALID")
                continue
            
            # if it passes all the checks
            # then first update the customer's budget:
            self.customerDetails[customerID - 1][self.BUDGET_INDEX] -= amount
            # then update the customer's total transactions for the day:
            self.customerDetails[customerID - 1][self.DAILY_TRANSACTIONS_INDEX] += 1
            # then add the transaction to our ledger, because this is a new one and
            # we hadn't seen it up until now:
            self.ledger.add((customerID, amount, pin))
            # and mark this transaction as VALID!
            checks.append("VALID")
            
        print("Final Details: " + str(self.customerDetails))
        return checks  

def main():
    solver = Solution()
    print(solver.solver(customerBudget = [1000, 2000, 5000], transactions = [[1, 200, 9191], [2, 225, 7364], [1, 80, 9191], [1, 300, 2222], [2, 350, 7364], [3, 240, 6146], [1, 80, 9191]]))
    
    solver = Solution()
    print(solver.solver(customerBudget = [100, 2000, 5000], transactions = [[1, 200, 9291], [2, 225, 7164], [1, 8000, 9291], [1, 300, 2222], [2, 350, 7364], [3, 240, 6146], [1, 80, 9291]]))
    
    solver = Solution()
    print(solver.solver(customerBudget = [100000, 2000, 5000], transactions = [[1, 200, 9291], [1, 225, 9291], [1, 8000, 9291], [1, 300, 9291], [1, 350, 9291], [1, 240, 9291], [1, 80, 9291], [1, 81, 9291], [1, 84, 9291], [1, 11, 9291], [1, 444, 9291], [1, 90, 9291], [1, 80, 9291], [1, 80, 9291], [2, 350, 7364], [3, 240, 6146], [3, 50001, 6146]]))
    
    # solver.solver()
    # solver.solver()
    # solver.solver()
    
if __name__ == "__main__":
    main()
