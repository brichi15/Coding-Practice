class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ##check horizontal and vertical
        
        
        for i in range(9):
            horTable = [0]*10
            verTable = [0]*10
            for j in range(9):

                horVal = board[i][j]
                verVal = board[j][i]
                
                if horVal != ".":
                    horVal = int(horVal)
                    horTable[horVal] += 1
                    if horTable[horVal] > 1:  return False
                    
                if verVal != ".":
                    verVal = int(verVal)
                    verTable[verVal] += 1
                    if verTable[verVal] > 1:  return False
                    
        for i in range(0,9,3):
            for j in range(0,9,3):
                
                table = [0]*10
                for l in range(3):
                    for m in range(3):
                        
                        val = board[i+l][j+m]
                        
                        if val != ".":
                            val = int(val)
                            table[val] += 1
                            if table[val] > 1 :return False
                            
        
        return True
                        