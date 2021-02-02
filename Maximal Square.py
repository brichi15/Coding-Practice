class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        
        def biggestSquareAtPoint(row,col):
            
            cur_max = 0
            
            while row<m and col<n and matrix[row][col] == "1":
                
                isSquare = True
                
                for i in range(1,cur_max+1):
                    
                    if matrix[row-i][col] != "1" or matrix[row][col-i] != "1":
                        isSquare = False
                        break
                    
                if not isSquare: break
                
                cur_max += 1
                row += 1
                col += 1 
            
            return cur_max
            
        cur_max = 0
        
        for row in range(m):
            for col in range(n):
                
                cur_max = max(cur_max,biggestSquareAtPoint(row,col))
                
        return cur_max**2