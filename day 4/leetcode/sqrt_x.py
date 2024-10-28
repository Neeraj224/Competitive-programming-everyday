class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, x):
        # pass
        # if x < 2:
        #     return x
        
        # left = 2
        # right = x // 2
        
        # while left <= right:
        #     pivot = left + (right - left) // 2
            
        #     if pivot * pivot > x:
        #         right = pivot - 1
        #     elif pivot * pivot < x:
        #         left = pivot + 1
        #     else:
        #         return pivot
        
        # return right
        
        if x == 0:
            return 0
        if x == 1:
            return 1

        low = 0
        high = x
        mid = (low + high) // 2
        
        while low < high:
            if mid * mid > x and not(low == high - 1):
                high = mid
                mid = (low + high) // 2
            elif mid * mid < x and not(low == high - 1):
                low = mid
                mid = (low + high) // 2
            elif low == high - 1:
                break
            else:
                return mid
        
        return mid

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(x = 4))
    print(solver.solver(x = 8))
    print(solver.solver(x = 10))

if __name__ == "__main__":
    main()