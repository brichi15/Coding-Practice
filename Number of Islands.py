class Solution:
    
    def dfs(self,grid,i,j):

        if not int(grid[i][j]):
            return
        
        grid[i][j] = 0
        
        m = len(grid)
        n = len(grid[0])
        
        if i-1 >-1 and int(grid[i-1][j]):
            self.dfs(grid,i-1,j)
            
        if j-1 >-1 and int(grid[i][j-1]):
            self.dfs(grid,i,j-1)    
    
        if i+1 <m and int(grid[i+1][j]):
            self.dfs(grid,i+1,j)
         
        if j+1 <n and int(grid[i][j+1]):
            self.dfs(grid,i,j+1)        
        
    def numIslands(self, grid):
        
        if len(grid) == 0:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        islandCnt = 0
        
        for i in range(m):
            for j in range(n):
                
                if int(grid[i][j]):
                    self.dfs(grid,i,j)
                    islandCnt +=1
                    
                    
        return islandCnt            
