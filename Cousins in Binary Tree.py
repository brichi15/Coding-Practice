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
        

## find both x and y at once:

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        def dfs(root):
            ans = [None,None,1,1]
            
            if not root:
                return ans
            
            if root.left:
                if root.left.val == x: ans[0] = root
                if root.left.val == y: ans[1] = root
            if root.right:
                if root.right.val == x: ans[0] = root
                if root.right.val == y: ans[1] = root
                
            if ans[0] != None or ans[1] != None: return ans
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left[0] != None: 
                ans[0] = left[0]
                ans[2] = left[2]+1
            elif right[0] != None:
                ans[0] = right[0]
                ans[2] = right[2]+1
            
            if left[1] != None: 
                ans[1] = left[1]
                ans[3] = left[3]+1
            elif right[1] != None:
                ans[1] = right[1]
                ans[3] = right[3]+1
            
            return ans
        
        res = dfs(root)
        
        if res[0] != None and res[1] != None and res[0] != res[1] and res[2] == res[3]: return True
        return False