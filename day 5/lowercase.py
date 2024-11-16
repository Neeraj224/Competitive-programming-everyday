"""
    709. To Lower Case
    
    Example 1:

    Input: s = "Hello"
    Output: "hello"
    Example 2:

    Input: s = "here"
    Output: "here"
    Example 3:

    Input: s = "LOVELY"
    Output: "lovely"
    
    Constraints:

    1 <= s.length <= 100
    s consists of printable ASCII characters.

"""
class Solution:
    def __init__(self):
        self.ALPHABETS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def test(self):
        print('a: ' + str(ord('a')))
        print('z: ' + str(ord('z')))
        
        print('A: ' + str(ord('A')))
        print('Z: ' + str(ord('Z')))

        print(ord('a') - ord('A'))
    
    def solver(self, s):
        # pass
        """
            using ord() we get its ascii code.
            using chr() we can convert it back to
            its printable character using the ascii code:
            
            ord('a') = 97
            chr(97) = 'a'
        """
        lowercase = ""

        for i in range(len(s)):
            if ord('a') <= ord(s[i]) <= ord('z'):
                lowercase += s[i]
            elif s[i] not in self.ALPHABETS:
                lowercase += s[i]
            else:
                lowercase += chr(ord(s[i]) + (ord('a') - ord('A')))
        
        return lowercase
            

def main():
    solver = Solution()
    
    print(solver.test())
    
    print(solver.solver(s = "Hello"))
    print(solver.solver(s = "here"))
    print(solver.solver(s = "LOVELY"))
    print(solver.solver(s = "xyzABC"))
    
    # solver.solver()
    # solver.solver()
    # solver.solver()
    
if __name__ == "__main__":
    main()