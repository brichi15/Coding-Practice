class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        
        def get_array(s):
            
            prev = None
            res = []
            for letter in s:
                if letter != prev:
                    res.append([letter,1])
                    prev = letter
                else:
                    res[-1][1] += 1
                
            return res
        
        s_arr = get_array(S)
        
        counter = 0
        for word in words:
            w_arr = get_array(word)
            
            if len(s_arr) != len(w_arr): continue
            
            stretchy = True
            for i in range(len(w_arr)):
                if s_arr[i][0] != w_arr[i][0]:
                    stretchy = False
                    break
                
                diff = s_arr[i][1] - w_arr[i][1]
                
                if diff < 0 or (diff > 0 and s_arr[i][1] <= 2):
                    stretchy = False
                    break
                
            if stretchy: counter += 1
                
        return counter