# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        queue = deque()
        queue.append((root,0))
        cur_left = root
        prev_level = 0
        while queue:
            node,level = queue.popleft()
        
            if level > prev_level:
                cur_left = node
                prev_level = level
                
            if node.left: queue.append((node.left,level+1))
            if node.right: queue.append((node.right,level+1))
        return cur_left.val