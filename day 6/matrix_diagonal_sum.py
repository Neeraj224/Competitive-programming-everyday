"""
    1572. Matrix Diagonal Sum
    
    Given a square matrix mat, return the sum of the matrix diagonals.
    Only include the sum of all the elements on the primary diagonal and all
    the elements on the secondary diagonal that are not part of the primary diagonal.
"""

class Solution:
    def __init__(self):
        self.container = []
    
    def get_left(self, matrix):
        i = 0
        j = 0
        
        while i < len(matrix) and j < len(matrix[0]):
            self.container.append(matrix[i][j])
            
            i += 1
            j += 1
        
    def get_right(self, matrix):
        i = len(matrix[0]) - 1
        j = 0
        
        while i >= 0 and j < len(matrix):
            if i == j:
                i -= 1
                j += 1
                continue
            
            self.container.append(matrix[i][j])
            
            i -= 1
            j += 1
    
    def solver(self, mat):
        # pass
        self.get_left(mat)
        self.get_right(mat)
        
        return sum(self.container)

def main():
    solver = Solution()
    print(solver.solver(mat = [[1,2,3], [4,5,6], [7,8,9]]))
    
    solver = Solution()
    print(solver.solver(mat = [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]))
    
    solver = Solution()
    print(solver.solver(mat = [[5]]))
    
    # solver.solver()
    # solver.solver()
    # solver.solver()
    
if __name__ == "__main__":
    main()
