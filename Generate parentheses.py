class Solution:
    def generateParenthesis(self, n: int) -> List[str]:  
        i = n               #stack counter for open brace
        j = 0               #stack counter for close brace
        
        def dfs(i,j,combo):
            
            if not i and not j:
                return [combo]
                
            cur_combo = []
                
            if i:
                cur_combo += dfs(i-1,j+1,combo + "(")
                
            if j:
                cur_combo += dfs(i,j-1,combo + ")")
                
            return cur_combo
                
        return dfs(i,j,"")