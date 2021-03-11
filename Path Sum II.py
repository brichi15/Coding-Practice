class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        
        res = []
        
        def dfs(node,combo,cur_sum):
            
            if not node:
                return
        
            cur_sum += node.val
            
            if not node.left and not node.right:
                if cur_sum == targetSum: res.append(combo+[node.val])
                return
            
            dfs(node.left,combo+[node.val],cur_sum)
            dfs(node.right,combo+[node.val],cur_sum)
            
        dfs(root,[],0)
        return res