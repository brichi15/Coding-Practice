class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices: return 0
        
        lowest = prices[0]
        
        m = 0
        
        for num in prices[1:]:
            
            if num < lowest:
                lowest = num
                
            else:
                m = max(m,num-lowest)
                
        return m
        