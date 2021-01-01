"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        
        not_possible = set()
        
        def isIn(root,target):
            
            if not root:
                return False
            
            if root == target:
                return True
            
            ans = False
            
            for child in root.children:
                if child not in not_possible:
                    not_possible.add(child)
                ans = ans or isIn(child,target)
                
            return ans
        
        candidate = tree[0]
        
        for node in tree[1:]:
            if node not in not_possible:
                if isIn(node,candidate):
                    candidate = node
                
        return candidate
                
        