class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        def getMaxSum(root):
            
            if not root.left and not root.right:
                return [root.val,root.val]
                
            left = right = [-1001,-1001]
            if root.left: left = getMaxSum(root.left)
            if root.right: right = getMaxSum(root.right)
            
            my_max_path = max(root.val + max(left[0],right[0]), root.val)
            
            
            general_max = max([my_max_path, left[0] + root.val + right[0], left[1], right[1]])
            
            return [my_max_path, general_max]
        
        return getMaxSum(root)[1]