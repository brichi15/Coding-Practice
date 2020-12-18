class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix) 
        
        def rotateLayer(n,scaler):
            
            for i in range(n-1):
                
                r0 = 0              +scaler
                c0 = 0      +i      +scaler

                r1 = 0      +i      +scaler
                c1 = n-1            +scaler

                r2 = n-1            +scaler
                c2 = n-1    -i      +scaler

                r3 = n-1    -i      +scaler
                c3 = 0              +scaler
                
                temp = matrix[r3][c3]
                matrix[r3][c3] = matrix[r2][c2]
                matrix[r2][c2] = matrix[r1][c1]
                matrix[r1][c1] = matrix[r0][c0]
                matrix[r0][c0] = temp

        scaler = 0
        
        for i in range(n,1,-2):
            
            rotateLayer(i,scaler)
            scaler += 1