class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.grid = []
        self.winState = 0
        self.size = n
        
        for i in range(n):
            row = [0]*n
            self.grid.append(row)
            
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        
        if self.grid[row][col] != 0:
            print("Error")
            return -1  ##error
        
        self.grid[row][col] = player
        
        winflags = [True, True, False, False]         # row = 0, col = 1, diag1 = 2, daig2 = 3        
        n = self.size
        
        ##check row
        for i in range(n):
            if self.grid[row][i] != player:
                winflags[0] = False
                break
        
        #check col
        for i in range(n):
            if self.grid[i][col] != player:
                winflags[1] = False
                break
                
        #check diag1 and 2
        
        if row == col:
            winflags[2] = True
            
            for i in range(n):
                if self.grid[i][i] != player:
                    winflags[2] = False
                    break
        
        if abs(n-row) == col or abs(n-row) == col +1:
            winflags[3] = True
            j = n-1
            for i in range(n):
                if self.grid[i][j] != player:
                    winflags[3] = False
                    break
                j -= 1
        
        
        if any(winflags):
            self.winState = player
            
        return self.winState


