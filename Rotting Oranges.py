from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)         
        n = len(grid[0])

        def bfs(queue):
            direct = [0,1,0,-1,0]
            level = 0
            while queue:
                row,col,level = queue.popleft()
                
                for i in range(4):
                    
                    n_row = row + direct[i]
                    n_col = col + direct[i+1]
                    
                    if n_row < 0 or n_row >= m: continue
                    if n_col < 0 or n_col >= n: continue
                    if grid[n_row][n_col] != 1: continue        #not fresh orange
                        
                    grid[n_row][n_col] = 2
                    queue.append((n_row,n_col,level+1))

            return level
        

        queue = deque()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row,col,0))
                    
        mins = bfs(queue)
                
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    return -1
                
        return mins
                