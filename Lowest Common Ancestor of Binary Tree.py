class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def postOrder(root,p,q):
            
            left = (None,None)
            right = (None,None)
            
            if root.left:
                left = postOrder(root.left,p,q)
            
            if root.right:
                right = postOrder(root.right,p,q)
            
            if left[0] and left[0] == left[1]:
                return left
            elif right[0] and right[0] == right[1]:
                return right
                
            ans = [None,None]
                
            if left[0] or right[0] or root == p:
                ans[0] = root
                
            if left[1] or right[1] or root == q:
                ans[1] = root
                
            return tuple(ans)
        
        return postOrder(root,p,q)[0]