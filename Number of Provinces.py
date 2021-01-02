class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)

        visited = set()
        
        def dfs(city1):
            
            visited.add(city1)
            
            for city2 in range(n):
                if isConnected[city1][city2] == 1:
                    if city2 not in visited:
                        dfs(city2)
                        
        res = 0         
        for i in range(n):
            
            if i not in visited:
                dfs(i)
                res += 1
        return res