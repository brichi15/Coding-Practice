class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        
        stack = 0
        table = {}
        
        max_len = 0
        
                
        for i,val in enumerate(nums):
            
            if val == 1:
                stack += 1                
            
            else:   #val == 0
                stack -= 1

            if stack == 0:
                max_len = max(max_len,i+1)
                
            if stack not in table:
                table[stack] = i
                continue
                
            max_len = max(max_len,i-table[stack])
            
            
        return max_len