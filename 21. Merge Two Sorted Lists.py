# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 == None: return l2
        if l2 == None: return l1
        
        if l1.val > l2.val:
            head = l2
            l2 = l2.next
            
            
        else:
            head = l1
            l1 = l1.next
            
        head.next = None
        ptr = head
        

        while l1 != None and l2 != None:
            
            if l1.val > l2.val:
                ptr.next = l2
                l2 = l2.next
                
            else:   
                ptr.next = l1
                l1 = l1.next
                
            ptr = ptr.next
            ptr.next = None    
                
        if l1 == None: ptr.next = l2
        else: ptr.next = l1
        
        return head