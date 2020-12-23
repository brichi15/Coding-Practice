class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        zhold = 0
        
        for i in range(n):
            
            if nums[i] != 0:
                
                temp = nums[zhold]
                nums[zhold] = nums[i]
                nums[i] = temp
                
                zhold += 1
