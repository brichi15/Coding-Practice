class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        left = None
        right = None
        
        m_ind = 0
        for i in range(1,len(nums)):
            
            if nums[m_ind] > nums[i]:
                right = i
            else:
                m_ind = i
            
        s_ind = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            
            if nums[s_ind] < nums[i]:
                left = i
            else:
                s_ind = i
                    
            
        if right == None:
            return 0
        
        else:
            return right-left + 1