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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int len = 0;
        for (ListNode* cur = head; cur; cur = cur->next)
            len++;
        int n = len / k, rest = len % k;
        ListNode* last = nullptr;
        vector<ListNode*> res(k, nullptr);
        
        for (int i = 0; head && i < k; i++, rest--) {
            res[i] = head;
            for (int j = 0; j < n + (rest > 0); j++) {
                last = head;
                head = head->next;
            }
            last->next = nullptr;
        }
        
        return res;
    }
};