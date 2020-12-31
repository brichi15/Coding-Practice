class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        goal = n-1
        
        visited = {}
        
        if n == 1:
            return 0
        
        def dfs(ind,steps):
            
            if ind == goal:
                return 1
            
            take = inf
            no_take = inf
                
            if steps >= 0:           ## try from next:
                temp = nums[ind]
                if (ind+1,temp-1) not in visited:
                    visited[(ind+1,temp-1)] = dfs(ind+1,temp-1)
                    
                take = 1 + visited[(ind+1,temp-1)]
                
                
            if steps > 0:
                if (ind+1,steps-1) not in visited:
                    visited[(ind+1,steps-1)] = dfs(ind+1,steps-1)
                no_take = visited[(ind+1,steps-1)]
                

            return min(take,no_take)
                
        return dfs(0,nums[0])