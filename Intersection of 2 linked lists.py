class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        visited = set()                # set
        
        
        while headA or headB:
            
            if headA in visited: return headA
            elif headA: 
                visited.add(headA)
                headA = headA.next
                
            if headB in visited: return headB
            elif headB: 
                visited.add(headB)
                headB = headB.next
        
        return None