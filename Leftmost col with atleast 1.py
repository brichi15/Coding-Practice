class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        m,n = binaryMatrix.dimensions()
        
        i = 0
        j = n-1
        
        leftMost = n
        
        while j >= 0 and i < m:
            
            if binaryMatrix.get(i,j) == 1:
                leftMost = min(leftMost,j)
                j -= 1
                
            else:
                i += 1
        
        if leftMost == n:
            return -1
        return leftMost
                