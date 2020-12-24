class Solution:
    def compress(self, chars: List[str]) -> int:
        
        cur_let = chars[0]
        let_count = 1
        ind = 0
        
        for i in range(1,len(chars)+1):
            
            if i < len(chars) and chars[i] == cur_let: let_count += 1
                
            else:
                chars[ind] = cur_let
                ind += 1
                if let_count > 1:
                    temp = list(str(let_count))
                    chars[ind:ind+len(temp)] = temp
                    ind += len(temp)
                    
                let_count = 1
                if i < len(chars): cur_let = chars[i]
                    
        return ind
        