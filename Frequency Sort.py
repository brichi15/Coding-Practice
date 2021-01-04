class Solution:
    def frequencySort(self, s: str) -> str:
        
        table = {}
        
        for letter in s:
            
            if letter not in table:
                table[letter] = 1
            
            else:
                table[letter] += 1
                
        table_list = list(table.items())
        
        table_list.sort(key= lambda x: x[1], reverse=True)
        
        res = ""
        
        for letter, freq in table_list:
            res += letter*freq
            
        return res
        