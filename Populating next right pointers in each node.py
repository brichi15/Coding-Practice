class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root: return root        
        
        curr_node = root
        level_root = root
        
        while curr_node.left:                   #assume perfect tree
            
            
            curr_node.left.next = curr_node.right           #link nodes children
            
            if curr_node.next: 
                curr_node.right.next = curr_node.next.left     #link current right to next left             
                curr_node = curr_node.next
            else:
                level_root = level_root.left
                curr_node = level_root
                
        return root
            