"""
    1275. Find Winner on a Tic Tac Toe Game
    
    Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the 
    ith move will be played on grid[rowi][coli]. return the winner of the game if 
    it exists (A or B). In case the game ends in a draw return "Draw". If there are 
    still movements to play return "Pending".

"""
class Solution:
    def __init__(self):
        self.gamegrid = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]
        self.STATUS = "PENDING"
        self.WINNER = "DRAW"
    
    def check_for_winner(self):
        def check_horizontally():
            for i in range(len(self.gamegrid)):
                if (self.gamegrid[i][0] != '.' and self.gamegrid[i][1] != '.' and self.gamegrid[i][2] != '.') and (self.gamegrid[i][0] == self.gamegrid[i][1] == self.gamegrid[i][2]):
                    self.WINNER = self.gamegrid[i][0]
        
        def check_vertically():
            for j in range(len(self.gamegrid)):
                if (self.gamegrid[0][j] != '.' and self.gamegrid[1][j] != '.' and self.gamegrid[2][j] != '.') and (self.gamegrid[0][j] == self.gamegrid[1][j] == self.gamegrid[2][j]):
                    self.WINNER = self.gamegrid[0][j]
        
        def check_diagonally():
            if self.gamegrid[0][0] != '.' and self.gamegrid[1][1] != '.' and self.gamegrid[2][2] != '.':
                if self.gamegrid[0][0] == self.gamegrid[1][1] == self.gamegrid[2][2]:
                    self.WINNER = self.gamegrid[0][0]
                    
            if self.gamegrid[0][2] != '.' and self.gamegrid[1][1] != '.' and self.gamegrid[2][0] != '.':
                if self.gamegrid[0][2] == self.gamegrid[1][1] == self.gamegrid[2][0]:
                    self.WINNER = self.gamegrid[0][2]
        
        check_horizontally()
        check_vertically()
        check_diagonally()
    
    def make_move(self, row, col, player):
        if player == 'A':
            self.gamegrid[row][col] = 'X'
        elif player == 'B':
            self.gamegrid[row][col] = 'O'
    
    def print_grid(self):
        print("\n")
        for row in self.gamegrid:
            print(row)
        print("\n")
    
    def who_won(self, symbol):
        if symbol == 'X':
            return 'A'
        elif symbol == 'O':
            return 'B'
    
    def solver(self, moves):
        n = len(moves)
        
        for i in range(n):
            if i % 2 == 0:
                self.make_move(moves[i][0], moves[i][1], 'A')
            else:
                self.make_move(moves[i][0], moves[i][1], 'B')
            
            self.print_grid()
            self.check_for_winner()
            
            if self.WINNER != "DRAW":
                return self.who_won(self.WINNER)

        if n == 9:
            return self.WINNER
        elif self.STATUS == "PENDING" and n < 9:
            return self.STATUS

def main():
    solver = Solution()
    print(solver.solver(moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]))
    
    solver = Solution()
    print(solver.solver(moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
    
    solver = Solution()
    print(solver.solver(moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))
    
    # solver.solver()
    # solver.solver()
    # solver.solver()
    
if __name__ == "__main__":
    main()