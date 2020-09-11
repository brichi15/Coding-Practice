class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        common = {}
        
        for letter in s:
            if letter not in common.keys(): common[letter] = 0
            else: common[letter] += 1
                
        for letter in t:
        
            if letter not in common.keys(): return False
            else: 
                common[letter] -= 1
                if common[letter] < 0: del common[letter]
        
        return not bool(common)
                    