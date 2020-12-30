# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        queue0 = [root]
        queue1 = []
        
        toggle = 0
        
        ans = []
        
        if not root: return ans
        
        while queue0 or queue1:
            
            if toggle == 0:
                node = queue0.pop(0)
                
                if node.left: queue1.append(node.left)
                if node.right: queue1.append(node.right)
                    
                if not queue0: 
                    ans.append(node.val)
                    toggle = 1
                
            else:
                node = queue1.pop(0)
                
                if node.left: queue0.append(node.left)
                if node.right: queue0.append(node.right)
                
                if not queue1: 
                    ans.append(node.val)
                    toggle = 0
                    
        return ans