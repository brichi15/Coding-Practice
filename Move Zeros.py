class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero_count = 0
        
        i=0                     ##iterator
        
        while i < len(nums):
            
            if nums[i] == 0:
                nums.pop(i)
                zero_count += 1
                
                
            else:
                i += 1
                
        nums += [0]*zero_count
            