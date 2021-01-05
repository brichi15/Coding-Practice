######################## DFS VERSION #######################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        def flatten(root):
            
            if not root.right and not root.left:
                return root
            
            tail = root
            
            if root.left:
                tail = flatten(root.left)
                right = root.right
                root.right = root.left
                root.left = None
                tail.right = right
                
            if tail.right:
                tail = flatten(tail.right)
                
            return tail
        
        flatten(root)
        

################# STACK VERSION #######################

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
                node.left = None
                
            if stack:
                node.right = stack[-1]
                