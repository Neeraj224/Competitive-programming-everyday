"""
    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
    You must do it in place.
    
"""  
class Solution:
    def __init__(self, matrix):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        
    def touch(self, matrix):
        for i in range(self.rows):
            for j in range(self.cols):
                if matrix[i][j] == 0:
                    # row persists first, so i,
                    # which means j will change:
                    for k in range(self.cols):
                        if matrix[i][k] == 0:
                            continue
                        else:
                            matrix[i][k] = '.'
                    
                    # col persists next, so, j,
                    # which means i will change:
                    for k in range(self.rows):
                        if matrix[k][j] == 0:
                            continue
                        else:
                            matrix[k][j] = '.'
    
    def conflate(self, matrix):
        for i in range(self.rows):
            for j in range(self.cols):
                if matrix[i][j] == '.':
                    matrix[i][j] = 0
    
    def solver(self, matrix):
        # pass
        self.touch(matrix = matrix)
        self.conflate(matrix = matrix)
        print(matrix)

def main():
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    solver = Solution(matrix)
    print(solver.solver(matrix))
    
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solver = Solution(matrix)
    print(solver.solver(matrix))
    # print(solver.solver())
    
    # solver.solver()
    # solver.solver()
    # solver.solver()
    
if __name__ == "__main__":
    main()