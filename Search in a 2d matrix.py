class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        row = 0
        col = n-1
        
        while row < m and col >= 0:
            
            if matrix[row][col] > target:       #go left
                col -= 1
                
            elif matrix[row][col] < target:      #go down
                row += 1
                
            else: # equal target
                return True
            
        return False