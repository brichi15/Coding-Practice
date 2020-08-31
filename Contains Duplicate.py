class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        exists = {}
        
        if len(nums) == 0:
            return 0
        
        for i in range(len(nums)):
            
            if nums[i] in exists.keys():
                return 1
            
            exists[nums[i]] = 1
        
        return 0