from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        deq = deque()
        res = []
        
        f_ptr = 0
        for b_ptr in range(len(nums)):
           
            while deq and nums[b_ptr] >= nums[deq[-1]]: deq.pop()    
            deq.append(b_ptr)
            
            if f_ptr > deq[0]: deq.popleft()
            
            if b_ptr >= k-1:
                res.append(nums[deq[0]])
                f_ptr += 1
                
        return res