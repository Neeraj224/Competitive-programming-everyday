class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, prices):
        # pass
        profit = 0
        
        lowest = prices[0]
        
        for price in prices:
            # if we find a lower price to buy at:
            if price < lowest:
                # update the lowest price
                lowest = price
            # get the max profit that can be achieved with the 
            # current price and the current lowest, compared to the
            # previous max profit and update:
            profit = max(profit, price - lowest)
        
        return profit

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(prices = [7, 1, 5, 3, 6, 4]))
    print(solver.solver(prices = [7, 6, 4, 3, 1]))
    # print(solver.solver())

if __name__ == "__main__":
    main()