class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        zero_holder = 0                               
        i = 0
        while i < len(nums):
        
            if nums[zero_holder] != 0:                  ## stop at first zero
                zero_holder += 1
                
            if nums[i] != 0 and i > zero_holder:        ##swap
                
                nums[zero_holder] = nums[i]
                nums[i] = 0
        
            
            i +=1
                        