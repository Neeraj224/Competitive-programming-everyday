class Solution:
    def __init__(self):
        pass
    
    def solver(self, s: str):
        if len(s) == 1:
            return True
        
        stack = ""
        stack += s[0]
        
        for i in range(1, len(s)):
            if stack * ((len(s) // len(stack))) == s:
                return True
            else:
                stack += s[i]
        
        return False
        
def main():
    solver = Solution()
    
    print(solver.solver(s = "abab"))
    print(solver.solver(s = "aba"))
    print(solver.solver(s = "abcabcabcabc"))
    
    # solver.solver()
    # solver.solver()
    # solver.solver()
    
if __name__ == "__main__":
    main()