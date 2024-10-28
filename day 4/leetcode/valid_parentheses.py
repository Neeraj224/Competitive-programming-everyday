class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, s):
        # pass
        stack = []
        balance = 0
        
        for c in s:
            if c == '(':
                stack.append(c)
                balance += 1
            elif c == '{':
                stack.append(c)
                balance += 1
            elif c == '[':
                stack.append(c)
                balance += 1
            elif c == ')':
                if stack[-1] == '(':
                    stack.pop()
                    balance -= 1
                else:
                    stack.append(c)
                    balance += 1
            elif c == '}':
                if stack[-1] == '{':
                    stack.pop()
                    balance -= 1
                else:
                    stack.append(c)
                    balance += 1
            elif c == ']':
                if stack[-1] == '[':
                    stack.pop()
                    balance -= 1
                else:
                    stack.append(c)
                    balance += 1
        
        return balance == 0
        

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(s = "()"))
    print(solver.solver(s = "()[]{}"))
    print(solver.solver(s = "(]"))
    print(solver.solver(s = "([]){}"))

if __name__ == "__main__":
    main()