class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        direct = [[1,2],[2,1],[-1,2],[-2,1],[-1,-2],[-2,-1],[1,-2],[2,-1]]
        
        memo = {}
        
        def dfs(r,c,K):
            
            if K <= 0:
                if (r >= 0 and r < N) and (c >= 0 and c < N):
                    return 1
                else:
                    return 0
            
            if (r < 0 or r >= N) or (c < 0 or c >= N):
                return 0
            
            count = 0
            for d in direct:
                new_r = r + d[0]
                new_c = c + d[1]
                
                if (new_r, new_c, K-1) not in memo:
                    memo[(new_r, new_c, K-1)] = dfs(new_r, new_c, K-1)
                
                count += memo[(new_r, new_c, K-1)]
                
            return count
        
        count = dfs(r,c,K)
        
        return count/(8**K)
            