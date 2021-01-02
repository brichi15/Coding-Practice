class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        
        def dfs(root,val):
            
            left = [None,0]            
            right = [None,0]
            
            if root.left:
                if root.left.val == val:
                    return [root,1]
                left = dfs(root.left,val)
                
            if root.right:
                if root.right.val == val:
                    return [root,1]
                right = dfs(root.right,val)
                
            if left[0]:
                left[1] += 1
                return left
                
            elif right[0]:
                right[1] += 1
                return right
            
            return [None,0]
        
        x_info = dfs(root,x)
        y_info = dfs(root,y)
        
        if x_info[1] == y_info[1] and x_info[0] != y_info[0]:
            return True
        return False
        