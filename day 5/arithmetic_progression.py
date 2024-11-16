"""
    Example 1:

    Input: arr = [3,5,1]
    Output: true
    Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
    Example 2:

    Input: arr = [1,2,4]
    Output: false
    Explanation: There is no way to reorder the elements to obtain an arithmetic progression.
    

    Constraints:
    2 <= arr.length <= 1000
    -10^6 <= arr[i] <= 10^6
"""
class Solution:
    def __init__(self):
        pass
    
    def solver(self, arr):
        # pass
        if len(arr) == 2:
            return True
        
        arr.sort()
        
        diff = arr[1] - arr[0]
        
        for i in range(1, len(arr) - 1):
            if arr[i + 1] - arr[i] != diff:
                return False
        
        return True

def main():
    solver = Solution()
    
    print(solver.solver(arr = [3,5,1]))
    print(solver.solver(arr = [1,2,4]))
    # print(solver.solver())
    
    # solver.solver()
    # solver.solver()
    # solver.solver()
    
if __name__ == "__main__":
    main()