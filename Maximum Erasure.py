class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        max_sum = 0
        cur_sum = 0
        front = 0
        visited = set()
        
        for i in range(n):
            
            while nums[i] in visited:
                cur_sum -= nums[front]
                visited.remove(nums[front])
                front += 1
            
            visited.add(nums[i])
            cur_sum += nums[i]
            max_sum = max(max_sum,cur_sum)
                
                
        return max_sum
                