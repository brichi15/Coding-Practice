class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def sameTree(root,t):
            
            if not root and not t:
                return True
            
            if not root and t or root and not t:
                return False
            
            if root.val != t.val:
                return False
            
            left = sameTree(root.left,t.left)
            right = sameTree(root.right,t.right)
            
            return left and right
        
        def checkRoot(s,t):
            
            if not s:
                return False
            
            ans = sameTree(s,t)
            
            if ans: return ans
            
            left = checkRoot(s.left,t)
            right = checkRoot(s.right,t)
                
            return left or right
        
        return checkRoot(s,t)