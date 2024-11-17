"""
    1041. Robot Bounded In Circle

    The robot can receive one of three instructions:
    "G": go straight 1 unit.
    "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
    "R": turn 90 degrees to the right (i.e., clockwise direction).
    The robot performs the instructions given in order, and repeats them forever.

    Return true if and only if there exists a circle in the plane such that the robot 
    never leaves the circle.
"""

class Solution:
    def __init__(self):
        # our direction vectors
        self.directions = {
            'N': [0, 1],
            'E': [1, 0],
            'S': [0, -1],
            'W': [-1, 0]
        }
        # initial vector:
        # the robot is at point (0, 0) and points to 'North'
        self.vector = [0, 0, 'N']
        
    def move(self):
        # add the distances/displacements according to the 
        # direction vectors
        self.vector[0] += self.directions[self.vector[2]][0]
        self.vector[1] += self.directions[self.vector[2]][1]

    def calibrate(self, turn):
        # turn anti-clockwise
        if turn == 'L':
            if self.vector[2] == 'N':
                self.vector[2] = 'W'
            elif self.vector[2] == 'W':
                self.vector[2] = 'S'
            elif self.vector[2] == 'S':
                self.vector[2] = 'E'
            elif self.vector[2] == 'E':
                self.vector[2] = 'N'
        # turn clockwise
        elif turn == 'R':
            if self.vector[2] == 'N':
                self.vector[2] = 'E'
            elif self.vector[2] == 'E':
                self.vector[2] = 'S'
            elif self.vector[2] == 'S':
                self.vector[2] = 'W'
            elif self.vector[2] == 'W':
                self.vector[2] = 'N'
            
    def solver(self, instructions):
        for instruction in instructions:
            # if we encounter a turn, we need to recalibrate
            # the direction in which the robot is gonna move
            if instruction == 'L' or instruction == 'R':
                self.calibrate(instruction)
            # else, we just need to move!
            elif instruction == 'G':
                self.move()
        
        # print the final vector:
        print(self.vector)
        
        # check the final vector:
        if self.vector[0] == self.vector[1] == 0 or self.vector[2] != 'N':
            return True
        else:
            return False

def main():
    solver = Solution()
    print(solver.solver(instructions = "GGLLGG"))
    
    solver = Solution()
    print(solver.solver(instructions = "GG"))
    
    solver = Solution()
    print(solver.solver(instructions = "GL"))
    
    # solver.solver()
    # solver.solver()
    # solver.solver()
    
if __name__ == "__main__":
    main()