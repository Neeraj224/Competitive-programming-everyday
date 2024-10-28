class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums, target):
        # pass
        index_map = {}

        for i in range(len(nums)):
            index_map[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in index_map and index_map[complement] != i:
                return [i, index_map[complement]]
        
        return []

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums = [2,7,11,15], target = 9))
    print(solver.solver(nums = [3,2,4], target = 6))
    print(solver.solver(nums = [3,3], target = 6))

if __name__ == "__main__":
    main()