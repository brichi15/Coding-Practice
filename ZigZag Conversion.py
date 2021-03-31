class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        data = [""]*numRows
        
        shift = 1           ##-1 = backward, 1= foward
        index = 0
        
        for let in s:
            
            data[index] += let 
            
            if (numRows-1) == 0: shift = 0
            elif index == 0: shift = 1
            elif index == (numRows -1): shift = -1
            
            index += shift
            
            
        
        return "".join(data)
                
            
            