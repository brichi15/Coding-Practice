class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0:
            return []
        
        res = [[1]]
        cur_len = 1
        
        for i in range(numRows-1):
            
            cur_len += 1
            cur_row = []
            for j in range(cur_len):
                
                if j-1 >= 0: left = res[i][j-1]
                else: left = 0
                    
                if j < cur_len-1: right = res[i][j]
                else: right = 0
                
                cur_row.append(left+right)
                
            res.append(cur_row)
            
        return res