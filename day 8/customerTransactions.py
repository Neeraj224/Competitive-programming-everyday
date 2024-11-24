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
        self.customerOrders = []
        self.customerDetails = []
        self.ledger = set()
            
    def solver(self, customerBudget, transactions):
        # pass
        for i in range(len(customerBudget)):
            # 0 -> id, 
            # 1 -> budget, 
            # 2 -> pin
            # 3 -> total daily transactions
            self.customerDetails.append([i + 1, customerBudget[i], -1, 0])
        
        for i in range(len(transactions)):
            if self.customerDetails[transactions[i][0] - 1][2] == -1:
                self.customerDetails[transactions[i][0] - 1][2] = transactions[i][2]
        
        print("Initial Details: " + str(self.customerDetails))
        checks = []
        
        for customerID, amount, pin in transactions:
            # print(customerID)
            # print(self.customerDetails[customerID - 1])
            
            if (customerID, amount, pin) in self.ledger:
                checks.append("DUPLICATE")
                continue
            
            if self.customerDetails[customerID - 1][3] >= 10:
                checks.append("INVALID")
                continue
            
            if amount > 50000:
                checks.append("INVALID")
                continue
            
            if self.customerDetails[customerID - 1][2] != pin:
                checks.append("INVALID")
                continue
            
            if amount > self.customerDetails[customerID - 1][1]:
                checks.append("INVALID")
                continue

            self.customerDetails[customerID - 1][1] -= amount
            self.customerDetails[customerID - 1][3] += 1
            self.ledger.add((customerID, amount, pin))
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