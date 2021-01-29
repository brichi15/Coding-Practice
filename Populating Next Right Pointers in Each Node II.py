from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        queue = deque()
        
        queue.append([root,0])
        
        prev_level = 0
        prev_node = None
        
        if not root:
            return root
        
        while queue:
            node,level = queue.popleft()
            if level > prev_level:
                prev_node = None
                prev_level = level
            
            if prev_node:
                prev_node.next = node
            prev_node = node
            
            if node.left:
                queue.append([node.left,level+1])
            if node.right:
                queue.append([node.right,level+1])
                
        return root