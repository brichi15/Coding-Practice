# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        
        def dfs(root,length):
            if not root:
                return length
            
            if root.left and root.val+1 == root.left.val:
                left = dfs(root.left,length+1)
            else:
                left = dfs(root.left,1)
                
            if root.right and root.val+1 == root.right.val:
                right = dfs(root.right,length+1)
            else:
                right = dfs(root.right,1)
                
            return max([left,right,length])
            
        return dfs(root,1)