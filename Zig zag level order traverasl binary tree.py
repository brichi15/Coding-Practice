class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root: return root
        
        q_for = [root]          #forward que
        s_rev = []              #reverse stack
        ans = []
        buffer = []
        f_or_r = 0
        empty_buff = False
        
        while q_for or s_rev:           #there are elements in the queue
                  
            if q_for and f_or_r == 0:                                               ## forward              
                temp_node = q_for.pop(0)                            #pop from front (queue)
                buffer.append(temp_node.val)                        # put value in buffer
                
                if temp_node.left:  s_rev.append(temp_node.left)    # append children left to right
                if temp_node.right: s_rev.append(temp_node.right)    
                    
                if not q_for: 
                    f_or_r = 1
                    empty_buff = True
                
                
            elif s_rev and f_or_r == 1:                                           #reverse               
                temp_node = s_rev.pop()                         # pop from back (stack)
                buffer.append(temp_node.val)
                
                if temp_node.right: q_for = [temp_node.right] + q_for
                if temp_node.left:  q_for = [temp_node.left] + q_for
                    
                    
                if not s_rev: 
                    f_or_r = 0
                    empty_buff = True
                    
            if empty_buff:
                empty_buff = False
                ans.append(buffer)
                buffer = []
            
        return ans