class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
    
        stack = []
        cur_node = root
        
        res = []
        
        while stack or cur_node:
            
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
                
            elif stack:
                cur_node = stack.pop()
                res.append(cur_node.val)
                cur_node = cur_node.right
        
        return res