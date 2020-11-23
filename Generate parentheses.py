class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        
        i = n               #stack counter for open brace
        j = 0               #stack counter for close brace

        combo = ""
        
        def dfs(i,j,combo):
            
            
            if not i and not j:
                res.append(combo)
                return
                
            if i and j:
                combo += "("                    ## add front brace
                dfs(i-1,j+1,combo)
                
                combo = combo[:-1]              ## remove front brace add back brace
                combo += ")"
     
                dfs(i,j-1,combo)
                
            elif j and not i:
                combo += ")"
                dfs(i,j-1,combo)
                
            else:
                combo += "("
                dfs(i-1,j+1,combo)
                
                
        dfs(i,j,combo)
        
        return res
            