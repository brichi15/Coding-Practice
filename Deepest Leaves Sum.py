# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        que = deque()
        que.append((root,0))
        
        p_depth = 0
        cur_sum = 0
        while que:
            node,depth = que.popleft()
            
            if depth > p_depth:
                cur_sum = 0
                p_depth = depth
                
            cur_sum += node.val
            
            if node.left: que.append((node.left,depth+1))
            if node.right: que.append((node.right,depth+1))
                
        return cur_sum