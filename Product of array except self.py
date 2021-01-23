class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        output = [0]*n
        
        cur_prod = 1
        for i in range(n):
            output[i] = cur_prod
            cur_prod *= nums[i]
            
        cur_prod = 1
        
        for i in range(n-1,-1,-1):
            output[i] *= cur_prod
            cur_prod *= nums[i]
            
        return output
        