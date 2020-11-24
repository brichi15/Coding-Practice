# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return None
        
        res = [root.val]
        q = [root]
        
        while q:
            node = q.pop(0)            
            
            if node.left:
                res.append(node.left.val)
                q.append(node.left)
            else:
                res.append("null")
                
                
            if node.right:
                res.append(node.right.val)
                q.append(node.right)
            else:
                res.append("null")
         
        return res            
            
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        i = 0        
        
        if not data: return None
        
        root = TreeNode(data[i])
        length = len(data)
        
        def dfs(root,i):
            
            li = i*2+1
            ri = i*2+2
            
            if li < length:
                root.left = TreeNode(data[li])
                dfs(root.left,li)
                
            if ri < length:
                root.right = TreeNode(data[ri])
                dfs(root.right,ri)
                
        dfs(root,i)
 
        return root
            
            
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))