/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if( !head || !head->next ) return true;
        
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* prev = NULL;
        
        while( fast && fast->next ) {
            fast = fast->next->next;
            ListNode* temp = slow->next;
            slow->next = prev;
            prev = slow;
            slow = temp;
        }
        // odd
        if ( fast != NULL ) { 
            slow = slow->next;
        }
        // compare
        while ( prev && slow ) { 
            if ( prev->val != slow->val ) return false;
            prev = prev->next;
            slow = slow->next;
        }
        if ( prev!=NULL || slow!=NULL ) return false;            
        return true;
    }
};
