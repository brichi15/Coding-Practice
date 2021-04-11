class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        memo = {}
        def longestIncreasing(row,col):
            
            direct = [0,1,0,-1,0]
            
            my_val = matrix[row][col]
            path_l = 0
            actual_l = 0
            
            for i in range(4):
                n_row = row+direct[i]
                n_col = col+direct[i+1]
                
                if n_row < 0 or n_row >= m: continue
                if n_col < 0 or n_col >= n: continue
                if my_val >= matrix[n_row][n_col]: continue
                
                if (n_row,n_col) not in memo:
                    memo[(n_row,n_col)] = longestIncreasing(n_row,n_col)
                n_path_l,n_actual_l = memo[(n_row,n_col)]
                
                path_l = max(path_l, n_path_l)
                actual_l = max(actual_l, n_actual_l)
                
            path_l += 1
            actual_l = max(actual_l, path_l)
            
            return (path_l,actual_l)
        
        max_path = 0
        
        for i in range(m):
            for j in range(n):
                
                max_path = max(max_path,longestIncreasing(i,j)[1])
                
        return max_path