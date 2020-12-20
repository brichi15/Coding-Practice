class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        letter_number = 0
        
        if not strs:
            return ""
        
        for letter in strs[0]:
            for word in strs[1:]:
                
                if letter_number >= len(word) or letter != word[letter_number]:  return strs[0][:letter_number]
                
            letter_number += 1
            
        return strs[0][:letter_number]