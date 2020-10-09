class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])
        
        i_zeros = []
        j_zeros = []
        
        for i in range(m):                          ## find the zeros
            for j in range(n):
                
                if matrix[i][j] == 0:
                    i_zeros.append(i)
                    j_zeros.append(j)
                    
        for i in i_zeros:
            matrix[i] = [0]*n
            
        for j in j_zeros:
            for i in range(m):
                matrix[i][j] = 0
                