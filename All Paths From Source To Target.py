class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        res = []
        
        def dfs(ind,path):
            
            if ind == n-1:
                res.append(path)
                
            for node in graph[ind]:
                dfs(node, path +[node])
        
        dfs(0,[0])
        return res