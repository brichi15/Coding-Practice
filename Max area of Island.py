lass Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        
        def dfs(i,j):
            
            
            grid[i][j] = 0            
            add = 1
            
            direct = [0,1,0,-1,0]
            for k in range(4):
                new_i = i + direct[k]
                new_j = j + direct[k+1]
                
                if new_i < 0 or new_i >= m:
                    continue
                if new_j < 0 or new_j >= n:
                    continue
                if grid[new_i][new_j] == 0:
                    continue
                
                add += dfs(new_i,new_j)
                        
            return add
            
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 1:
                    res = max(res,dfs(i,j))
                
        return res