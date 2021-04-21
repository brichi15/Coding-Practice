class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        def dfs(root):
            
            if not root:
                return [0,0]
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            return [max(left[0],right[0])+1,max([left[1],right[1],left[0]+right[0]])]
        
        return dfs(root)[1]