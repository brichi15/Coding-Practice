class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        lengthPrices = len(prices)
        
        h = -1
        i = 0
        j = 1
            
        buyFlag = 0
        
        while(i < lengthPrices):

            ival = prices[i]
            
            if(h > -1): hval = prices[h]
            else: hval = ival    
            
            if(j < lengthPrices): jval = prices[j]
            else: jval = ival
                
            if(ival-hval <= 0 and jval-ival > 0 and buyFlag == 0 ): 
                buyPrice = ival
                buyFlag = 1
                
            elif(ival-hval > 0 and jval-ival <= 0 and buyFlag == 1 ):
                maxProfit += ival - buyPrice
                buyFlag = 0
                
            print(buyFlag)
                
            h += 1
            i += 1
            j += 1
            
        return maxProfit
                