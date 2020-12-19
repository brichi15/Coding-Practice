class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        stack = [-(2**31 +1)]
        
        def dfs(root):
            
            left = True
            right = True
            
            if root.left:
                left = dfs(root.left)
            
            if root.val <= stack[-1]:
                return False
            
            stack.append(root.val)
            
            if root.right:
                right = dfs(root.right)
                
            return left and right
            
        return dfs(root)