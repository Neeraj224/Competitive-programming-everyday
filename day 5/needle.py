class Solution:
    def __init__(self):
        pass
    
    def solver(self, haystack: str, needle: str):
        if len(needle) > len(haystack):
            return -1
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        
        return -1
                    

def main():
    solver = Solution()
    
    print(solver.solver(haystack = "sadbutsad", needle = "sad"))
    print(solver.solver(haystack = "leetcode", needle = "leeto"))
    # solver.solver()
    
if __name__ == "__main__":
    main()