class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode(0,None)
        ptr = head
        
        while l1 or l2 or carry:
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            t_sum = val1+val2+carry
            carry = int(t_sum/10)
            digit = t_sum%10
            
            ptr.next = ListNode(digit,None)
            ptr = ptr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return head.next