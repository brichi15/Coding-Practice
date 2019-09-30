class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""
        
        sr = list(s[n::-1])         ##reverse string
        s = list(s)
            
        
        ss1 = ""
        ss0 = "" 
        i=0
        for i in range(1,n+1):
            ss0 = s[0:i]            ##sliding window both ways
            ss1 = sr[n-i:n]
            
            ss2 = sr[0:i]
            ss3 = s[n-i:n]

            j=0
            pal0 = ""
            pal1 = ""
            for j in range(len(ss0)):

                if ss0[j] == ss1[j]:            ## collect consective equivalent letters
                    pal0 = pal0 + ss0[j]
                    
                    if (len(pal0) > len(ans)) and (pal0[0] == pal0[len(pal0)-1]):
                        ans = pal0

                else:
                    pal0 = ""
                    
                    
                if ss2[j] == ss3[j]:
                    pal1 = pal1 + ss2[j]
                    
                    if (len(pal1) > len(ans)) and (pal1[0] == pal1[len(pal1)-1]):
                        ans = pal1

                else:
                    pal1 = ""    
         
        return "".join(ans)