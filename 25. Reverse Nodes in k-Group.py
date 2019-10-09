# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverseLinkedList(head: ListNode) -> ListNode:          ##reverses linked list and returns head of new

    prev = head
    cur = head.next
    if prev.next != None: nex = cur.next
    else: return head

    prev.next = None        ##first cycle edge case
    cur.next = prev

    while nex != None:

        prev = cur
        cur = nex
        nex = nex.next

        cur.next = prev

    return cur    


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        
        front_node = head       ## front of group
        cut_node = head         ## back of group
        back_node = head        ## back connecting point
        prefront_node = head    ## front connecting point
        
        
        first_cycle = 1
        
        while cut_node != None:
            
            for i in range(k-1):                              ## traverse k times to identify section
                cut_node = cut_node.next
                if cut_node == None: return head
            
            if cut_node != None:
                back_node = cut_node.next
                cut_node.next = None
            
            
            front_node = reverseLinkedList(front_node)      ## reverse sectioned group
            
            if first_cycle == 1:                               ##if first cycle, store head 
                first_cycle = 0         ##no longer first cycle
                head = front_node
            else:
                prefront_node.next = front_node
                
            while front_node.next != None:                ##traverse to end
                front_node = front_node.next
                
            
            front_node.next = back_node
            
            prefront_node = front_node
            front_node = back_node
            cut_node = back_node
            
        return head         
            