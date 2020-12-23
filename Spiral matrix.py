class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)
        n = len(matrix[0])
        
        i = 0
        j = 0
        
        visited = set()
        state = 0
        
        res = []
        
        
        while (i,j) not in visited:
            
            res.append(matrix[i][j])
            visited.add((i,j))
            
            if state == 0:
                if j+1 < n and (i,j+1) not in visited:
                    j += 1
                else:
                    state = 1
                    if i+1 < m: i += 1
                    
            elif state == 1:
                if i+1 < m and (i+1,j) not in visited:
                    i += 1
                else:
                    state = 2
                    if j-1 >= 0: j -= 1
                    
            elif state == 2:
                if j-1 >= 0 and (i,j-1) not in visited:
                    j -= 1
                else:
                    state = 3
                    if i-1 >= 0: i -= 1
            
            else:
                if i-1 >= 0 and (i-1,j) not in visited:
                    i -= 1
                else:
                    state = 0
                    if j+1 < n: j += 1
                
            
        return res
                