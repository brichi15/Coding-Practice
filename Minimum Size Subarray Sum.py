class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        front = 0
        back = 0
        
        n = len(nums)
        res = n +1
        
        cur_sum = 0
        
        while back <= n:
            
            if cur_sum < s:
                if back < n: cur_sum += nums[back]
                back += 1
                

            else:
                res = min(res,back-front)
                cur_sum -= nums[front]
                front += 1
        
        if res >= n+1:
            return 0
        
        return res