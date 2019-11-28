class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        
        if s == '' or s == ' ' : return 0
        
        val = '';
        index = -1
        count = 0
        
        val = s[index]
        
        if val != ' ':
            count += 1
            index += -1
            try:
                val = s[index]
            except:
                return count
            
        while val == ' ':
            index += -1
            try:
                val = s[index]
            except:
                break
            
        while val != ' ':
            count += 1
            index += -1
            try:
                val = s[index]
            except:
                break
        
        return count
            