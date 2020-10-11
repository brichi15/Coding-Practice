class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        length = len(s)
        visited = {}            ##visited table for letters
        
        i = 0
        
        ans = 0
        
  
        for j in range(length):
            
            if s[j] not in visited: visited[s[j]] = 1
            else: 
                while s[i] != s[j]:                         ## remove element up to repeat
                    del visited[s[i]]
                    i += 1                                  ## dont need to remove s[j] instance
                i += 1                                      ## i index in front of repeated element
            
            if j+1-i > ans:
                ans = j+1-i
                
        return ans