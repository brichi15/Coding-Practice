class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        front = 0
        back = 0
        
        table = {}
        n = len(s)
        max_len = 0
        while back <= n:
            
            if len(table) > 2:
                table[s[front]] -= 1
                if table[s[front]] == 0:
                    del table[s[front]]
                front += 1
            
            else: 
                max_len = max(max_len,back-front)
                if back < n:
                    if s[back] not in table: table[s[back]] = 0
                    table[s[back]] += 1
                back += 1
                
        return max_len