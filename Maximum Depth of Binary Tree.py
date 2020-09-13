# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return depthDFS(root)
        
        
    
def depthDFS(root: TreeNode) -> int:
    if root == None:
        return 0
    elif root.left == None and root.right == None:
        return 1
    else:
        depth = max(1 + depthDFS(root.left), 1 + depthDFS(root.right))
        return depth