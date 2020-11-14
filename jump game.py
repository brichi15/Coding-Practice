class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        length = len(nums)
        
        i = 0
        step = nums[0]
        
        while step >= 0:
            
            step = max(step,nums[i])
            
            if(i+step >= length-1): return True
            
            step -= 1
            i += 1
        return False
            