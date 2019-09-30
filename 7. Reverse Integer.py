class Solution:
    def reverse(self, x: int) -> int:
        
        
        val = list(str(x))

        size = len(val)
        
        for i in range(int(size/2)):
            temp = val[i]
            val[i] = val[size-1-i]
            val[size-1-i] = temp
        
        val = "".join(val)
        
        if val[-1] == "-":
            val = '-' + val[:-1]
        
        val = int(val)
        if abs(val) > 2**31:
            return 0
            
        return val