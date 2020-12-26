class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        n = len(cost)
        
        visited = {}
        
        def dfs(ind):
            
            if ind >= n-1:
                return 0
            
            if ind+1 not in visited:
                visited[ind+1] = dfs(ind+1)
            one = cost[ind+1] + visited[ind+1]
            
            
            two = 0
            if ind+2 not in visited:
                visited[ind+2] = dfs(ind+2)
            if ind+2 < n: two = cost[ind+2] + visited[ind+2]
            
            
            return min(one,two)
        
        return dfs(-1)