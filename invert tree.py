class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def dfs(root):
            
            if not root: return root
            
            if not root.left and not root.right:
                return root
            
            temp = root.left
            root.left = root.right
            root.right = temp
            
            if root.left: dfs(root.left)
            if root.right: dfs(root.right)
            
            return root
        
        return dfs(root)
        

        