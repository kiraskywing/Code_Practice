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
    bool hasCycle(ListNode *head) {
        if (!head || !head->next)
            return false;

        ListNode *slow = head, *fast = head->next;
        while (fast->next && fast->next->next && slow != fast) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        return fast == slow;
    }
};