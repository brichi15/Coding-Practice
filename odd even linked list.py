class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
         
        odd = head
        counter = None
        if head: counter = head.next
            
            
        while counter:
            
            temp = counter.next                             ## remove odd value
            if (counter and counter.next): 
                counter.next = counter.next.next
                
             
            if temp: 
                temp.next = odd.next                            ## insert odd value
                odd.next = temp

        
            counter = counter.next
            odd = odd.next
            
            
        return head