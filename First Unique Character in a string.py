class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        chars = {}
        
        count = 0
        
        for char in s:
            
            if char in chars.keys():
                chars[char] = len(s)
                
            else:
                chars[char] = count
                
            count += 1
                
        
        val = len(s)
        
        for char in chars:
            if chars[char] != len(s) and chars[char] < val:
                val = chars[char]
                
        if val == len(s): val = -1
        return val      
            