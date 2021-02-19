class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        sum_table = {0: -1}
        cur_sum = 0
        max_length = 0
        
        for i in range(n):
            
            cur_sum += nums[i]
            
            if cur_sum-k in sum_table:
                max_length = max(max_length,i-sum_table[cur_sum-k])
            
            if cur_sum not in sum_table:
                sum_table[cur_sum] = i
                
        return max_length