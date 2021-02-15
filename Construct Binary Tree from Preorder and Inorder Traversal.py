class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        
        root = TreeNode(0,None,None)
        
        def formSubtrees(root,preorder,inorder):
            
            if not inorder:
                return None
            
            root.val = preorder[0]
            r_ind = inorder.index(root.val)
            
            root.left = formSubtrees(TreeNode(0,None,None),preorder[1:r_ind+1],inorder[:r_ind])
            root.right = formSubtrees(TreeNode(0,None,None),preorder[r_ind+1:],inorder[r_ind+1:])
            
            return root
        
        return formSubtrees(root,preorder,inorder)