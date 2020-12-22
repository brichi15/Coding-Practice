class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def helper(i):
            
            pal1 = ""
            pal2 = ""
            
            j = i
            k = i    
            while j >= 0 and k < len(s):
                if s[j] != s[k]:
                    break
                
                j -= 1
                k += 1
                
            pal1 = s[j+1:k]
            
            j = i
            k = i+1    
            while j >= 0 and k < len(s):
                if s[j] != s[k]:
                    break
                
                j -= 1
                k += 1
                
            pal2 = s[j+1:k]
            

            if len(pal1) >= len(pal2):
                return pal1
            else:
                return pal2
        
        res = ""
        
        for i in range(len(s)):
            temp = helper(i)
            
            if len(temp) > len(res): res = temp
            
        return res
            