# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        to_delete = set(to_delete)
        
        
        def dfs(root):
            
            if not root:
                return []
            
            ans = []
            ans += dfs(root.left)
            ans += dfs(root.right)
            
            if root.left and root.left.val in to_delete:
                if root.left.left:
                    ans.append(root.left.left)
                if root.left.right:
                    ans.append(root.left.right)
                root.left = None
                
            if root.right and root.right.val in to_delete:
                if root.right.left:
                    ans.append(root.right.left)
                if root.right.right:
                    ans.append(root.right.right)
                root.right = None

            return ans
        
        ans = dfs(root)
        
        if root.val not in to_delete:
            ans.append(root)
        else:
            if root.left:
                ans.append(root.left)
            if root.right:
                ans.append(root.right)
            
        return ans
            