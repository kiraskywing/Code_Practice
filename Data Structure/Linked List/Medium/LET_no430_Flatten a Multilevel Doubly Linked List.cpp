/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
public:
    Node* flatten(Node* head) {
        for (Node* cur = head; cur; cur = cur->next) {
            if (cur->child) {
                Node* nxt = cur->next;
                cur->next = cur->child;
                cur->child->prev = cur;
                cur->child = nullptr;
                Node* nxt2 = cur->next;
                while (nxt2->next)
                    nxt2 = nxt2->next;
                nxt2->next = nxt;
                if (nxt)
                    nxt->prev = nxt2;
            }
        }
        
        return head;
    }
};