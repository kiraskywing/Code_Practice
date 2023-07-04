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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int m = getSize(headA), n = getSize(headB);
        if (n > m) {
            swap(headA, headB);
            swap(m, n);
        }

        for (int i = m - n; i > 0; i--)
            headA = headA->next;

        while (headA && headA != headB) {
            headA = headA->next;
            headB = headB->next;
        }

        return headA;
    }

    int getSize(ListNode *head) {
        int count = 0;
        while (head) {
            count++;
            head = head->next;
        }
        return count;
    }
};