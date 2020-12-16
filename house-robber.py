class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums: return 0
        
        
        visited = dict()
        
        
        def dfs(ind):
            
        
            if ind >= len(nums): return 0

            if ind+2 in visited: p1 = visited[ind+2]
            else: 
                p1 = dfs(ind+2)
                visited[ind+2] = p1
                
            if ind+3 in visited: p2 = visited[ind+3]
            else: 
                p2 = dfs(ind+3)
                visited[ind+3] = p2
        
            return nums[ind] + max(p1,p2)
                
                
        first = dfs(0)
        second = dfs(1)
        
        
        return max(first,second)