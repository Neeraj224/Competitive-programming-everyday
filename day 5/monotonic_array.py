"""
    896. Monotonic Array:
    
    Example 1:

    Input: nums = [1,2,2,3]
    Output: true
    Example 2:

    Input: nums = [6,5,4,4]
    Output: true
    Example 3:

    Input: nums = [1,3,2]
    Output: false
    

    Constraints:

    1 <= nums.length <= 10^5
    -10^5 <= nums[i] <= 10^5

"""
class Solution:
    def is_monotonic_increasing(self, arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        
        return True
        
    
    def is_monotonic_decreasing(self, arr):
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                return False
        
        return True
    
    def solver(self, nums):
        if len(nums) == 1:
            return True
        
        if self.is_monotonic_increasing(nums) != False or self.is_monotonic_decreasing(nums) != False:
            return True
        else:
            return False

def main():
    solver = Solution()
    
    print(solver.solver(nums = [1,2,2,3]))
    print(solver.solver(nums = [6,5,4,4]))
    print(solver.solver(nums = [1,3,2]))
    
    # solver.solver()
    # solver.solver()
    # solver.solver()
    
if __name__ == "__main__":
    main()