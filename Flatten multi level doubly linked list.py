"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        if not head:
            return head
        
        def dfs_flatten(head):

            if not head.next and not head.child:
                return head
            
            tail = head
            if head.child:
                nex = head.next
                tail = dfs_flatten(head.child)
                head.next = head.child
                head.child.prev = head
                head.child = None
                
                tail.next = nex
                if nex: nex.prev = tail
                
            if tail.next:
                tail = dfs_flatten(tail.next)
                
            return tail
        
        dfs_flatten(head)
        return head