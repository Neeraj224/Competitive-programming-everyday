class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, x1, v1, x2, v2):
        # pass
        will_meet = "NO"
        for i in range(10001):
            if x1 == x2:
                will_meet = "YES"
                break
            x1 += v1
            x2 += v2
        
        return will_meet

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(0, 3, 4, 2))
    print(solver.solver(0, 2, 5, 3))
    # print(solver.solver())

if __name__ == "__main__":
    main()