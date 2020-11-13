class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
    
        if not root: return root
        
        return recurse(root)
        
        
        
def recurse(root):
    
    ans = []
    l = []
    r = []
    
    if root.left: l = recurse(root.left)    
    if root.right: r = recurse(root.right)
        
    ans += l+ [root.val] +r
    
    return ans