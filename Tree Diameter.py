class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        tree = {}
        
        for n1,n2 in edges:
            
            if n1 not in tree: tree[n1] = []
            if n2 not in tree: tree[n2] = []
                
            tree[n1].append(n2)
            tree[n2].append(n1)
            
        visited = set()
        def searchForDiameter(node):
            
            if node in visited:
                return [0,0]
            
            visited.add(node)
            
            first = 0
            second = 0
            cur_diam = 0
            
            for nex in tree[node]:
                
                depth,diam = searchForDiameter(nex)
                cur_diam = max(diam,cur_diam)
                
                if depth > first:
                    second = first
                    first = depth
                elif depth > second:
                    second = depth
                    
            visited.remove(node)
            
            return [first+1,max(cur_diam,first+second)]
                    
                
        return searchForDiameter(0)[1]