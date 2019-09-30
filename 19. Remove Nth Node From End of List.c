/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    
    struct ListNode* front;
    struct ListNode* back;
    struct ListNode* back1;
    
    front = head;
    back = head;
    back1 = head;
    
    int i = 0;
    
    while(front)
    {
        front = front->next;
        if(i>=n)
        {
            back = back->next;  
            if(i>=n+1) back1 = back1->next;
        }   
        
        i++;
    }
    
    if(back->next)
    {
        back->val = back->next->val;
        back->next = back->next->next; 
    }
    else
    {
        if(i == 1) head = NULL;
        else back1->next = NULL;
    }
    
    return head;
    
    
}