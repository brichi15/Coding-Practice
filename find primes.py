class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n < 2:
            return 0
        
        res = 0
        
        non_prime = set()
        
        for i in range(2,n):
            
            if i in non_prime:
                continue
        
            res += 1
            for j in range(i*i,n,i):
                non_prime.add(j)
        
        return res