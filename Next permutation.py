class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        i = n-2
        
        while i >= 0:
            prev = i+1
            
            if nums[prev] > nums[i]:  break
            i -= 1
        
        if i == -1:
            nums.reverse()
            return
            
        j = i+1
        
        while j < n and nums[i] < nums[j]: j += 1
        
        j -= 1
        
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
        temp = nums[i+1:]
        temp.reverse()
        nums[i+1:] = temp