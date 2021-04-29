class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        cur_sum = 0
        
        n = len(nums)

        table = {0:1}
        count = 0
        
        for i in range(n):
            cur_sum += nums[i]
            
            if cur_sum-k in table:
                count += table[cur_sum-k]
                
            
            if cur_sum not in table: table[cur_sum] = 1
            else: table[cur_sum] += 1
            
        return count