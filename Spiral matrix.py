class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        
        l_bound = 0
        u_bound = 0
        r_bound = len(matrix[0])
        d_bound = len(matrix)
        
        while True:
            
            for i in range(l_bound,r_bound):
                res.append(matrix[u_bound][i])
            u_bound += 1
            if u_bound >= d_bound: break
            
            for i in range(u_bound,d_bound):
                res.append(matrix[i][r_bound-1])    
            r_bound -= 1
            if r_bound <= l_bound: break
            
            for i in range(r_bound-1, l_bound-1, -1):
                res.append(matrix[d_bound-1][i])    
            d_bound -= 1
            if d_bound <= u_bound: break
            
            for i in range(d_bound-1,u_bound-1, -1):
                res.append(matrix[i][l_bound])
            l_bound += 1
            if l_bound >= r_bound: break
            
        return res