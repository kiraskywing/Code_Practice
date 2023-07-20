/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* parent;
};
*/

class Solution {
public:
    Node* lowestCommonAncestor(Node* p, Node * q) {
        unordered_set<Node*> memo;
        
        while (p) {
            memo.insert(p);
            p = p->parent;
        }
        
        while (q) {
            if (memo.count(q))
                return q;
            q = q->parent;
        }

        return nullptr;
    }
};