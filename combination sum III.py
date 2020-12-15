class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        output = []        
        combo = []
        
        def helper(combo,n,s):
            
            if len(combo) == k and n == 0:
                output.append(combo)
                return
            
            if k < 0 or n < 0: return
            
            for num in range(s,10):
                
                if num > n: continue
                
                s+=1 
                helper(combo+[num],n-num,s)
        
        helper(combo,n,1)
        
        return output