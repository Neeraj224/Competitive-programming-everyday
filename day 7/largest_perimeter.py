"""
    976. Largest Perimeter Triangle
    
    Given an integer array nums, return the largest perimeter of a triangle 
    with a non-zero area, formed from three of these lengths. If it is 
    impossible to form any triangle of a non-zero area, return 0.

    NOTE: Sum of the lengths of any two sides of a triangle must always be
    greater than the length of the third side of the triangle!

"""

class Solution:
    def __init__(self):
        pass
    
    def solver(self, nums):
        # pass
        nums.sort()
        
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        
        return 0

def main():
    solver = Solution()
    print(solver.solver(nums = [2, 1, 2]))
    
    solver = Solution()
    print(solver.solver(nums = [1, 2, 1, 10]))
    
    # solver = Solution()
    # print(solver.solver())
    
    # solver.solver()
    # solver.solver()
    # solver.solver()
    
if __name__ == "__main__":
    main()