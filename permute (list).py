class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        
        def dfs(nums):
            
            if len(nums) == 1: return [nums]
            
            length = len(nums)
            
            perms = []
            
            for i in range(length):
                for perm in dfs(nums[:i] + nums[i+1:]):
                    perms.append([nums[i]] + perm)
                    
            return perms
        
        return dfs(nums)