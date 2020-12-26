# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        
        def dfs(root,isLeft):
            
            if not root:
                return 0
            
            if isLeft and (not root.left) and (not root.right):
                return root.val
            
            left = 0
            right = 0
            
            if root.left:
                left = dfs(root.left,True) 
                
            if root.right:
                right = dfs(root.right,False)
                            
            return left+right
            
        return dfs(root,False)