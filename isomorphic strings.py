class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        t_table = dict()
        s_table = dict()
        
        for s_letter, t_letter in zip(s,t):
            
            if s_letter in s_table and t_letter not in t_table: return False
            elif s_letter not in s_table and t_letter in t_table: return False
            
            elif s_letter in s_table and t_letter in t_table:
                if s_table[s_letter] != t_letter: return False
                elif t_table[t_letter] != s_letter: return False
                
            else: 
                s_table[s_letter] = t_letter
                t_table[t_letter] = s_letter
                
        return True