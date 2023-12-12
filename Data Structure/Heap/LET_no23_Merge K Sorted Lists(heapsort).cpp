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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto cmp = [](ListNode* left, ListNode* right){ return left->val > right->val; };
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> pq(cmp);
        for (ListNode* node : lists) {
            if (node)
                pq.push(node);
        }
        ListNode* dummy = new ListNode();
        ListNode* head = dummy;
        while (!pq.empty()) {
            ListNode* cur = pq.top();
            pq.pop();
            head->next = cur;
            head = head->next;
            cur = cur->next;
            if (cur)
                pq.push(cur);
        }

        return dummy->next;
    }
};