class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1: return l2
        
        if not l2: return l1
        
        if l1.val < l2.val: 
            root = l1
            other = l2
        else: 
            root = l2
            other = l1
                
        main = root
        
        while main.next and other:
            
            if main.next.val > other.val:
                
                temp = main.next
                main.next = other
                other = other.next
                main.next.next = temp
                main = main.next
                
            else:
                main = main.next
                
                
        if other: main.next = other
        
        return root