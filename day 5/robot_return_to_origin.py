"""
    657. Robot Return to Origin
    
    Constraints:
    1 <= moves.length <= 2 * 104
    moves only contains the characters 'U', 'D', 'L' and 'R'.
"""

class Solution:
    def __init__(self):
        # pass
        self.movement = {
            'L': (-1, 0),
            'R': (1, 0),
            'U': (0, 1),
            'D': (0, -1)
        }
    
    def solver(self, moves):
        # pass
        initial_position = [0, 0]
        moved = [0, 0]
        
        for move in moves:
            if move == 'L':
                moved[0] += self.movement['L'][0]
                moved[1] += self.movement['L'][1]
            if move == 'R':
                moved[0] += self.movement['R'][0]
                moved[1] += self.movement['R'][1]
            if move == 'U':
                moved[0] += self.movement['U'][0]
                moved[1] += self.movement['U'][1]
            if move == 'D':
                moved[0] += self.movement['D'][0]
                moved[1] += self.movement['D'][1]
        
        return moved[0] == initial_position[1] and moved[1] == initial_position[1]
            
                

def main():
    solver = Solution()
    
    print(solver.solver(moves = "UD"))
    print(solver.solver(moves = "LL"))
    print(solver.solver(moves = "UDUULLRLDU"))
    
    # solver.solver()
    # solver.solver()
    # solver.solver()
    
if __name__ == "__main__":
    main()