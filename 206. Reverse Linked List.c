/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    
    if(head == NULL) return head;
    
    struct ListNode* cur;
    struct ListNode* prev;
    struct ListNode* next;
    
    cur = head;
    next = head->next;
    
    while(cur)
    {
        if(cur == head) cur->next = NULL;
        
        else cur->next = prev;
    
        prev = cur;
        cur = next;
        
        if(next)next = next->next;
    }
    
    return prev;
    
}

//------------------------------recursive----------------------------//
'''
    def revHelper(prev,head):
        if not head:
            return prev
        
        nex = head.next
        head.next = prev

        return revHelper(head,nex)
        

    return revHelper(None,head)
'''