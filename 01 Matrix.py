class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        
        def bfs(row,col):
            
            queue = [[row,col,0]]
            direct = [0,1,0,-1,0]
            visited = set()
            
            while queue:
                row,col,dist = queue.pop(0)
                if matrix[row][col] == 0:
                     return dist
                     
                visited.add((row,col))
            
                for i in range(4):
                    n_row = row+direct[i]
                    n_col = col+direct[i+1]
                    
                    if n_row < 0 or n_row >= m: continue
                    if n_col < 0 or n_col >= n: continue
                    if (n_row,n_col) in visited: continue
                     
                    queue.append([n_row,n_col,dist+1])
                    
        
        for row in range(m):
            for col in range(n):
                     
                if matrix[row][col] != 0:
                     matrix[row][col] = bfs(row,col)
        return matrix