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
    void reorderList(ListNode* head) {
        if (!head)
            return;
        
        ListNode *slow = head, *fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        ListNode *cur = slow->next, *last = nullptr;
        slow->next = nullptr;
        
        while (cur) {
            ListNode *nxt = cur->next;
            cur->next = last;
            last = cur;
            cur = nxt;
        }
        
        ListNode *head2 = head;
        while (last) {
            ListNode *nxt = head2->next;
            head2->next = last;
            head2 = head2->next;
            last = nxt;
        }
    }
};