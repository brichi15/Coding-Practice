class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        res = []
        def genCombos(n,k,num,combo):
        
            if num > 10 or k < 0 or n < 0:
                return
            
            if k == 0 and n == 0:
                res.append(combo)
                return
            
            genCombos(n-num,k-1,num +1,combo + [num])
            genCombos(n, k, num+1, combo)
            
        genCombos(n,k,1,[])    
        
        return res