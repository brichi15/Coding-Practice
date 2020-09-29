class Solution:
    def climbStairs(self, n: int) -> int:
        
        visited = {}
        
        return dfs(0,n,visited)

        
def dfs(curr_n,goal,visited):

        
    if(curr_n > goal): return 0

    if(curr_n == goal): return 1
    
    if(curr_n+1 in visited): sum1 = visited[curr_n+1]
    else:
        sum1 = dfs(curr_n+1,goal,visited)
        visited[curr_n+1] = sum1
    
    if(curr_n+2 in visited): sum2 = visited[curr_n+2]
    else:
        sum2 = dfs(curr_n+2,goal,visited)
        visited[curr_n+2] = sum2
  
    tsum = sum1 + sum2
        
    return tsum