class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        memo = {}
        
        def maximizePath(ind):
            
            two = 0
            three = 0
            
            if ind+2 < n: 
                if ind+2 not in memo: memo[ind+2] = maximizePath(ind+2)
                two = nums[ind+2] + memo[ind+2]
                
            if ind+3 < n: 
                if ind+3 not in memo: memo[ind+3] = maximizePath(ind+3)
                three = nums[ind+3] + memo[ind+3]
            
            return max(two,three)
        
        return maximizePath(-2)