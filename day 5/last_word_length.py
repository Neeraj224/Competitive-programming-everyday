"""
    58. Length of Last Word
    
    Input: s = "Hello World"
    Output: 5
    Explanation: The last word is "World" with length 5.

    Input: s = "   fly me   to   the moon  "
    Output: 4
    Explanation: The last word is "moon" with length 4.

    Input: s = "luffy is still joyboy"
    Output: 6
    Explanation: The last word is "joyboy" with length 6.

    Constraints:

    1 <= s.length <= 10^4
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.

"""

class Solution:
    def __init__(self):
        pass
    
    def solver(self, s):
        i = len(s) - 1
        
        length = 0
        started = False
        
        while i >= 0:
            if s[i] == ' ' and started == False:
                i -= 1
                continue
            elif s[i] != ' ':
                length += 1
                started = True
            elif s[i] == ' ' and started == True:
                break
            
            i-= 1
        
        return length
                

def main():
    solver = Solution()
    
    print(solver.solver(s = "Hello World"))
    print(solver.solver(s = "   fly me   to   the moon  "))
    print(solver.solver(s = "luffy is still joyboy"))
    
    # solver.solver()
    # solver.solver()
    # solver.solver()
    
if __name__ == "__main__":
    main()