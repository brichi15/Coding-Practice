class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        def dfs(root):
            
            right = 0
            left = 0
            
            if not root: return 0
            
            if not root.left and not root.right: return 1
            
            if root.right: 
                right = dfs(root.right)
                
            if root.left:  
                left = dfs(root.left)

            return 1+ right + left
                
        return dfs(root)

            
            
            
        