"""
    LC 13. Roman to Integer
    Example 1:

    Input: s = "III"
    Output: 3
    Explanation: III = 3.
    Example 2:

    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.
    Example 3:

    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    

    Constraints:

    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].

"""
class Solution:
    def __init__(self):
        # pass
        self.map = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }
    
    def solver(self, s):
        # pass
        i = len(s) - 1
        
        integer = 0
        
        while i >= 0:
            if s[i] == 'V':
                if i != 0 and s[i - 1] == 'I':
                    integer += self.map['IV']
                    i -= 2
                    continue
            if s[i] == 'X':
                if i != 0 and s[i - 1] == 'I':
                    integer += self.map['IX']
                    i -= 2
                    continue
            if s[i] == 'L':
                if i != 0 and s[i - 1] == 'X':
                    integer += self.map['XL']
                    i -= 2
                    continue
            if s[i] == 'C':
                if i != 0 and s[i - 1] == 'X':
                    integer += self.map['XC']
                    i -= 2
                    continue
            if s[i] == 'D':
                if i != 0 and s[i - 1] == 'C':
                    integer += self.map['CD']
                    i -= 2
                    continue
            if s[i] == 'M':
                if i != 0 and s[i - 1] == 'C':
                    integer += self.map['CM']
                    i -= 2
                    continue
            
            integer += self.map[s[i]]
            i -= 1
        
        return integer
            

def main():
    solver = Solution()
    
    print(solver.solver(s = "III"))
    print(solver.solver(s = "LVIII"))
    print(solver.solver(s = "MCMXCIV"))
    
    # solver.solver()
    # solver.solver()
    # solver.solver()
    
if __name__ == "__main__":
    main()