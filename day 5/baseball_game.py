"""
    682. Baseball Game
    
    Constraints:

    1 <= operations.length <= 1000
    operations[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 104, 3 * 104].
    For operation "+", there will always be at least two previous scores on the record.
    For operations "C" and "D", there will always be at least one previous score on the record.
"""

class Solution:
    def __init__(self):
        # pass
        self.record_stack = []
    
    def sum_previous(self):
        self.record_stack.append(self.record_stack[-1] + self.record_stack[-2])
    
    def double_record_stack(self):
        self.record_stack.append(2 * self.record_stack[-1])

    def invalidate_previous(self):
        self.record_stack.pop()
    
    def total(self):
        return sum(self.record_stack)
    
    def solver(self, ops):
        # pass
        for operation in ops:
            if operation == '+':
                self.sum_previous()
            elif operation == 'D':
                self.double_record_stack()
            elif operation == 'C':
                self.invalidate_previous()
            else:
                self.record_stack.append(int(operation))
        
        return self.total()

def main():
    solver = Solution()
    print(solver.solver(ops = ["5","2","C","D","+"]))
    
    solver = Solution()
    print(solver.solver(ops = ["5","-2","4","C","D","9","+","+"]))

    solver = Solution()
    print(solver.solver(ops = ["1","C"]))
    
    # solver.solver()
    # solver.solver()
    # solver.solver()
    
if __name__ == "__main__":
    main()