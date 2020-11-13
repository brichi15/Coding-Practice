class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = l1
        carry = 0

        while l1:
            
            if l2: l1.val += l2.val + carry
            else: l1.val += carry
                
            carry = 0
            
            
            if l1.val > 9:                      #update carry if necessary
                carry = int(l1.val/10)
                l1.val = l1.val%10
                
            if (not l1.next) and ((l2 and l2.next) or carry > 0):   ##if l1 done l2 not done or carry, add new node to l1
                l1.next = ListNode(0,None)
                
            l1 = l1.next
            if l2: l2 = l2.next
                
                
            
                
        return head