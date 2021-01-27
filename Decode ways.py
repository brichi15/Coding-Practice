class Solution:
    def numDecodings(self, s: str) -> int:
        
        ##letters = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ## consider 0 edge case

        memo = {}
            
        def createCombos(s):
            if not s:
                return 1
            
            ans = 0
            if s[0] != '0':
                if s[1:] not in memo:
                    memo[s[1:]] = createCombos(s[1:])
                ans += memo[s[1:]]
                
                if len(s) > 1 and int(s[:2]) <= 26:
                    if s[2:] not in memo:
                        memo[s[2:]] = createCombos(s[2:])
                    ans += memo[s[2:]]
                
            return ans
        
        return createCombos(s)
