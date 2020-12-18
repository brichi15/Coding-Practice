##memoized solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return amount
        
        visited = {}        
        
        def dfs(cur_sum):
            
            if cur_sum > amount:
                return amount+1
            elif cur_sum == amount:
                return 0
            
            ans = amount+1
            
            for coin in coins:
                
                if cur_sum+coin in visited:
                    temp = visited[cur_sum+coin]
                else:
                    temp = dfs(cur_sum+coin)
                    visited[cur_sum+coin] = temp
                    
                ans = min(ans, temp+1)
                    
            return ans
        
        res = dfs(0)
        
        return res if res <= amount else -1

## tabulated solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount+1]*(amount+1)
        
        dp[0] = 0
        
        coins.sort()
        
        for i in range(1, amount+1):
            for coin in coins:
                
                if coin <= i:
                    dp[i] = min(dp[i], 1+dp[i-coin])
                else:
                    break
        
        return dp[amount] if dp[amount] != amount+1 else -1