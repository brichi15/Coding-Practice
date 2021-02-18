class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        m = len(board)
        n = len(board[0])
        
        direct = [0,1,0,-1,0]
        visited = set()
        
        def findWord(row,col,ind):
            
            if board[row][col] != word[ind]: return False
            if ind == len(word)-1: return True
            
            visited.add((row,col))
            
            res = False
            for i in range(4):
                n_row = row + direct[i]
                n_col = col + direct[i+1]
                
                if n_row < 0 or n_row >= m: continue
                if n_col < 0 or n_col >= n: continue    
                if (n_row,n_col) in visited: continue
                    
                res = res or findWord(n_row,n_col,ind+1)
                
            visited.remove((row,col))
            return res
        
        for row in range(m):
            for col in range(n):
                if findWord(row,col,0):
                    return True
        return False