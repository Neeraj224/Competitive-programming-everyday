class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, s):
        # pass
        all_magic_squares = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        ]
        
        min_cost = float('inf')
        
        for magic_square in all_magic_squares:
            cost = 0
            
            for i in range(3):
                for j in range(3):
                    cost += abs(s[i][j] - magic_square[i][j])
            
            min_cost = min(min_cost, cost)
        
        return min_cost

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]))
    print(solver.solver(s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]))
    # print(solver.solver())

if __name__ == "__main__":
    main()