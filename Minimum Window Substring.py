class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        s_table = {}
        t_table = {}
        
        for letter in t:
            if letter not in t_table:
                t_table[letter] = 0
            t_table[letter] += 1

        front = 0
        back = 0 
        
        n = len(s)
        min_len = n+1
        min_str = ""
        while back <= n:
            
            enough = True
            for letter in t_table:
                if letter not in s_table or s_table[letter] < t_table[letter]: 
                    enough = False
                    break
                    
            if not enough:
                if back >= n: break
                if s[back] not in s_table:
                    s_table[s[back]] = 0
                s_table[s[back]] += 1
                back += 1
                
            else:   #enough
                if back-front < min_len:
                    min_len = back-front
                    min_str = s[front:back]
                s_table[s[front]] -= 1
                front += 1
                
        return min_str
                    