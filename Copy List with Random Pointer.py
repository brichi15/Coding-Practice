"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        cur_node = head
        cpy_node = cpy_head = Node(0)
        table = {}
        
        if not head:
            return head
        
        while cur_node:
            cpy_node.val = cur_node.val
            
            table[cur_node] = cpy_node
            
            if cur_node.next:
                cpy_node.next = Node(0)
            
            cur_node = cur_node.next
            cpy_node = cpy_node.next
            
        cur_node = head
        cpy_node = cpy_head
        
        while cur_node:
            if cur_node.random:
                cpy_node.random = table[cur_node.random]
            cur_node = cur_node.next
            cpy_node = cpy_node.next
            
        return cpy_head