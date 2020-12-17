class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        target = 0
        for num in nums: target += num
        
        target = target/2
    
        table = {}
        
        def dfs(ind,cur_sum):
            
            if cur_sum > target or ind >= len(nums):
                return False
            
            if cur_sum == target:
                return True
            
            if (ind+1,cur_sum) in table: no_add = table[(ind+1,cur_sum)]
            else:
                no_add = dfs(ind+1,cur_sum) 
                table[(ind+1,cur_sum)] = no_add
            
            if (ind+1,cur_sum + nums[ind]) in table: add = table[(ind+1,cur_sum + nums[ind])]
            else:
                add = dfs(ind+1,cur_sum + nums[ind])
                table[(ind+1,cur_sum + nums[ind])] = add
            
            return no_add or add
        
        return dfs(0,0)