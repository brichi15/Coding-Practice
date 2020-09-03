class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ind = 0
        hold = nums[0]    #start at index 0   
        
        visited = {}
        
        
        for i in range(len(nums)):
            
            if( ind in visited.keys()):
                ind += 1%len(nums)
                hold = nums[ind]
            
            visited[ind] = 1
            
            ind = (ind + k)%len(nums)
            
            tmp = nums[ind]
            nums[ind] = hold
            hold = tmp
        
            