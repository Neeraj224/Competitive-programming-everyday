class Solution:
    def __init__(self):
        pass
    
    def buildSystem(self, coordinates):
        # lets say we have: [1,2],[2,3]
        # so x2: a[1][0] | x1: a[0][0]
        # y2: a[1][1] | y1: a[0][1]
        x_diff = coordinates[1][0] - coordinates[0][0]
        y_diff = coordinates[1][1] - coordinates[0][1]
        
        if x_diff == 0:
            self.slope = 'inf'
        else:
            self.slope = y_diff / x_diff
    
    def getDistance(self, far, near):
        if (far[0] - near[0]) == 0 and self.slope == 'inf':
            return True
        elif (far[0] - near[0]) != 0:
            if ((far[1] - near[1]) / (far[0] - near[0])) == self.slope:
                return True

        return False
    
    def solver(self, coordinates):
        # pass
        if len(coordinates) == 2:
            return True
        
        self.buildSystem(coordinates = coordinates)
        # print(self.slope)
        n = len(coordinates) - 1
        
        for i in range(1, n):
            print(coordinates[i])
            if self.getDistance(coordinates[i + 1], coordinates[i]) == False:
                return False
        
        return True

def main():
    solver = Solution()
    print(solver.solver(coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
    
    solver = Solution()
    print(solver.solver(coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
    
    solver = Solution()
    print(solver.solver([[1,2],[2,3],[3,5]]))
    
    # solver.solver()
    # solver.solver()
    # solver.solver()
    
if __name__ == "__main__":
    main()