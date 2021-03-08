# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        
        children = {}
        
        def populateChildren(root):
            
            if root.left:
                children[root.left] = root
                populateChildren(root.left)
            
            if root.right:
                children[root.right] = root
                populateChildren(root.right)
                
        populateChildren(root)
        
        queue = deque()
        queue.append((target,0))
        
        visited = set()
        
        res = []
        while queue:
            node,level = queue.popleft()
            
            if node in visited:
                continue
            visited.add(node)
            
            if level == K:
                res.append(node.val)
                continue
                
            if node.left: queue.append((node.left,level+1))
            if node.right: queue.append((node.right,level+1))
            if node in children: queue.append((children[node],level+1))
        return res