class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, s, d, m):
        # pass
        if len(s) < m:
            return 0
        
            
        good_segments = 0
        for i in range(len(s) - m + 1):
            if sum(s[i : i + m]) == d:
                good_segments += 1
        
        return good_segments

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver([2, 2, 1, 3, 2], 4, 2))
    print(solver.solver([1, 2, 1, 3, 2], 3, 2))
    print(solver.solver([1, 1, 1, 1, 1, 1], 3, 2))
    print(solver.solver([4], 4, 1))
    

if __name__ == "__main__":
    main()