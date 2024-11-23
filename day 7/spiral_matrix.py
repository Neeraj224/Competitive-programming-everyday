"""
54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.
"""

class Solution:
    # def __init__(self):
    #     self.directions = {
    #         'R': [0, 1],
    #         'D': [1, 0],
    #         'L': [0, -1],
    #         'U': [-1, 0]
    #     }
       
    def solver(self, matrix):
        result = []
        
        # we'll use four pointers, and keep contracting them down
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        # while the corresponding pointers do not collide:
        while left < right and top < bottom:
            # we go left to right first, getting every 
            # element in the top row {first row}:
            for j in range(left, right):
                # the column is changing, so top's value (row) persists
                result.append(matrix[top][j])
            # after the first row is done, we increment top's value:
            top += 1
            
            # next we get every element in the rightmost column:
            for i in range(top, bottom):
                # the row is changing, so right - 1 (column's value) persists
                result.append(matrix[i][right -1])
            # after that, we update our right pointer:
            right -= 1
            
            if not (left < right and top < bottom):
                # this is for cases where we have only just one column,
                # or just one row in the matrix:
                # [1, 2, 3, 4]
                # or
                # [1,
                #  2,
                #  3,
                #  4]
                break
            
            # next, we get every element in the bottom row:
            # we go from column right - 1 to column left - 1:
            for j in range(right - 1, left - 1, -1):
                # since the column is changing:
                result.append(matrix[bottom - 1][j])
            # update the bottom pointer:
            bottom -= 1
            
            # now we get every element in the leftmost column:
            # also, we go from row bottom - 1 to row top - 1:
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        
        return result
                

def main():
    solver = Solution()
    print(solver.solver(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    
    solver = Solution()
    print(solver.solver(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]))

if __name__ == "__main__":
    main()
