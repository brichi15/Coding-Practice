# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        
        que = deque()
        que.append(root)
        
        parent = {}

        while que:
            node = que.popleft()
        
            if node.right:
                if node.right in parent: break
                parent[node.right] = node
                que.append(node.right)
        
            if node.left: 
                parent[node.left] = node
                que.append(node.left)
                
        bad_parent = parent[node]
        if bad_parent.left == node: bad_parent.left = None
        else: bad_parent.right = None
            
        return root