from heapq import heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        heap = []
        
        head = None
        
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap,(lists[i].val,i))
        
        if heap:
            ind = heappop(heap)[1]
            head = lists[ind]
            cur = head
        
            lists[ind] = cur.next
            if lists[ind]:
                    heappush(heap,(lists[ind].val,ind))
            
        while heap:
            ind = heappop(heap)[1]
            cur.next = lists[ind]
            cur = cur.next
            lists[ind] = cur.next
            
            if lists[ind]:
                heappush(heap,(lists[ind].val,ind))
        
        return head