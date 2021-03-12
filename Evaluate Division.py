class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        n = len(equations)
        
        graph = {}
        for i in range(n):                          ##generate graph
            var1,var2 = equations[i]
            
            if var1 not in graph: graph[var1] = {}
            if var2 not in graph: graph[var2] = {}
                
            graph[var1][var2] = values[i]
            graph[var2][var1] = 1/values[i]

        visited = set()
        def dfs(var,goal):                                             ##dfs to find if path to goal
            
            if var not in graph or goal not in graph: return -1
            if var in visited: return -1
            if var == goal: return 1
            
            visited.add(var)
            
            for node in graph[var]:
                val = graph[var][node]
                
                test = dfs(node,goal)
                if test > 0:
                    visited.remove(var)
                    return test*val
                    
            visited.remove(var)
            return -1
                
        res = []
        
        for query in queries:                           ##compute for each query
            var1,var2 = query
            div = dfs(var1,var2)
            if div > 0:
                if var2 not in graph[var1]:             ##update table if valid
                    graph[var1][var2] = div
                    graph[var2][var1] = 1/div
            res.append(div)
        return res
            