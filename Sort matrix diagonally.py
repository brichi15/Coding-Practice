class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])
        
        def helper(i,j):
            
            temp = []
            start = [i,j]
            
            while i < m and j < n:
                temp.append(mat[i][j])
                i += 1
                j += 1
            
            temp.sort()
            
            i = start[0]
            j = start[1]
            
            for num in temp:
                mat[i][j] = num
                i += 1
                j += 1
        
        i = m-1                       #beginning point
        j = 0
        
        while j < n:
            
            helper(i,j)
            
            if i > 0: i -= 1    
            else: j += 1
                
        return mat