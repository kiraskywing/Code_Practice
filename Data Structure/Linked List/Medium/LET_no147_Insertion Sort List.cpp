/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        if (!head || !(head->next))
            return head;
        
        ListNode* dummy = new ListNode(0, head);
        ListNode *prev = dummy;
        
        while (head) {
            if (head->next && head->next->val < head->val) {
                while (prev->next && prev->next->val < head->next->val)
                    prev = prev->next;
                
                ListNode* temp = prev->next;
                prev->next = head->next;
                head->next = head->next->next;
                prev->next->next = temp;
                prev = dummy;
            }
            else
                head = head->next;
        }
        
        return dummy->next;
    }
};