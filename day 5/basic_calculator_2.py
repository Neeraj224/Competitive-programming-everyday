class Solution:
    def __init__(self):
        self.NUMBERS = "0123456789"
        self.OPS = "+-/*"
    
    def contract(self, s):
        return ''.join(c for c in s if c != ' ')
    
    def solver(self, s):
        # NOTE: we need to consider / and * as the same
        # and because of that, we just need to parse it left to right

        s = self.contract(s)
        stack = []
        num = 0
        # arbitrary sign - we begin witha positive result
        # we will be checking trailing signs and performing 
        # the operation previous to it, by keeping the next one in the buffer
        sign = '+'
        
        for i, c in enumerate(s):
            if c in self.NUMBERS:
                # num can be more than two digits
                # so we need to keep building it
                # by parsing until we reach an operator
                num = num * 10 + int(c)

            if c in self.OPERATORS or i == len(s) - 1:
                if sign == '+':
                    # for the addition operator, we are just appending
                    # it to the stack because we will later on the sum the tack anyway
                    stack.append(num)
                elif sign == '-':
                    # same for the subtraction:
                    # push the -ve of that number to the stack
                    # so that when we sum the entire stack we utilise the negative sign
                    # for subtraction!
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    # can't use int division since python by default floors it
                    stack.append(int(stack.pop() / num))
                
                # update sign!
                sign = c
                # update num
                num = 0
        
        return sum(stack)

def main():
    solver = Solution()
    print(solver.solver("3+2*2"))
    print(solver.solver(" 3/2 "))
    print(solver.solver(" 3+5 / 2 "))
    print(solver.solver("0-2147483647"))
    print(solver.solver("2+3*4"))

if __name__ == "__main__":
    main()
