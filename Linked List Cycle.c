/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    
    if(head == NULL) return false;
    
    struct ListNode* front;
    struct ListNode* back;
    
    back = head;
    front = head->next;
    
    while(front)
    {
        if(front == back) return true;
        
        if(front->next)front = front->next->next;
        else front = front->next;
        back = back->next;    
    }
    return false;
}