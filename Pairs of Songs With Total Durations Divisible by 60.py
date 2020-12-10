class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        ans = 0
        table = {}
        
        for i,song in enumerate(time):
            
            remainder = song%60
            
            if (60-remainder)%60 in table:
                ans += len(table[(60-remainder)%60])
            
            if remainder not in table:
                table[remainder] = [i]
                
            else:
                table[remainder].append(i)
        
        return ans