class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        n = len(s)
        wordDict = set(wordDict)
        
        memo = {}
        
        def generatePossible(ind,combo):
            
            if ind >= n:
                if combo in wordDict: return True
                return False
            
            if (ind+1,combo+s[ind]) not in memo:
                memo[(ind+1,combo+s[ind])] = generatePossible(ind+1, combo + s[ind])
            res = memo[(ind+1,combo+s[ind])]
            
            if combo in wordDict:
                if (ind+1,s[ind]) not in memo:
                    memo[(ind+1,s[ind])] = generatePossible(ind+1, s[ind])
                res = res or memo[(ind+1,s[ind])]
                
            return res
        
        return generatePossible(0,"")