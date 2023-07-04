/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node)
            return node;
        
        unordered_map<Node*, Node*> memo;
        queue<Node*> q;
        q.push(node);
        
        while (!q.empty()) {
            Node* cur = q.front();
            q.pop();

            if (!memo.count(cur))
                memo[cur] = (cur ? new Node(cur->val) : nullptr);

            for (Node* nei : cur->neighbors) {
                if (!memo.count(nei)) {
                    memo[nei] = (nei ? new Node(nei->val) : nullptr);
                    if (nei)
                        q.push(nei);
                }
                
                memo[cur]->neighbors.push_back(memo[nei]);
            }
        }

        return memo[node];
    }
};