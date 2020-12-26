class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        min_diff = inf
        close = -1
        
        while root:
            
            cur_diff = abs(root.val - target)
            
            if min_diff > cur_diff:
                min_diff = cur_diff
                close = root.val
                
            
            if target < root.val:
                if not root.left: break
                root = root.left
            
            elif target >= root.val:
                if not root.right: break
                root = root.right
                
        return close
            