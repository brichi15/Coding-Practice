struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    
    struct ListNode *headNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode *curNode;
    struct ListNode *addNode;
    
    headNode->val = 0;
    headNode->next = NULL;
    curNode = headNode;
    
    int sum;
    int l1val;
    int l2val;
    int carry = 0;
    
    while(carry != 0 || l1 || l2)
    {   
        
        if(l1) l1val = l1->val;
        else l1val = 0;
        if(l2) l2val = l2->val;
        else l2val = 0;
        
        sum = carry +l1val + l2val;
        carry = sum/10;
        sum = sum%10;
        
        curNode->val = sum;
        
        if(l1) l1 = l1->next;
        if(l2) l2 = l2->next;
        
        
        if(carry!=0 || l1 || l2)
        {
        addNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        addNode->next = NULL;
        addNode->val = 0;
        curNode->next = addNode;
        curNode = curNode->next;
        }
    }    
    return headNode;
    
    
    
    
}