# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1
        
        if l1.val <= l2.val:
            head = l1
            ptr = l2
            
        else:
            head = l2
            ptr = l1
        
        ins = head
        while ptr:
            if ptr.val >= ins.val and (not ins.next or ptr.val < ins.next.val):
                temp = ptr.next
                ptr.next = ins.next
                ins.next = ptr
                ptr = temp
                
            ins = ins.next
            
        return head