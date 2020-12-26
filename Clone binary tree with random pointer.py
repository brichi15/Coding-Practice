class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        
        
        copy = NodeCopy(None,None,None,None)
        
        table = {}
        
        if not root:
            return root
        
        
        def dfs(root,copy):   
            
            
            table[root] = copy
            copy.val = root.val
            
            if root.left:
                copy.left = NodeCopy()
                dfs(root.left,copy.left)
            
            if root.right:
                copy.right = NodeCopy()
                dfs(root.right,copy.right)
            
        dfs(root,copy)
        
        def dfs2(root,copy):
            
            if root.random:
                copy.random = table[root.random]
            
            if root.left:
                dfs2(root.left,copy.left)
            if root.right:
                dfs2(root.right,copy.right)
            
        dfs2(root,copy)
        
        return copy