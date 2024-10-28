class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, nums1, m, nums2, n):
        # pass
        first = m - 1
        second = n - 1
        third = m + n - 1

        while second >= 0:
            if first >= 0 and nums1[first] > nums2[second]:
                nums1[third] = nums1[first]
                first -= 1
                third -= 1
            else:
                nums1[third] = nums2[second]
                second -= 1
                third -= 1

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
    print(solver.solver(nums1 = [1], m = 1, nums2 = [], n = 0))
    print(solver.solver(nums1 = [0], m = 0, nums2 = [1], n = 1))

if __name__ == "__main__":
    main()