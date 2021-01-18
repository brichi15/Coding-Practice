# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        stack = []
        node = root
        flag = 0
        
        while stack or node:
            
            if node:
                stack.append(node)
                node = node.left
                
            elif stack:
                node = stack.pop()
                if node == p:
                    flag = 1
                elif flag == 1:
                    return node
                    
                node = node.right