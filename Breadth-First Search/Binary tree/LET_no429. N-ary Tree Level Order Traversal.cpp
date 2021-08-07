/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        if (!root)
            return {};
        
        vector<vector<int>> res;
        queue<Node*> q;
        q.push(root);
            
        while (!q.empty()) {
            vector<int> cur_level;
            
            int n = q.size();
            for (int i = 0; i < n; i++) {
                Node* cur = q.front();
                q.pop();
                cur_level.push_back(cur->val);
                for (Node* child : cur->children)
                    q.push(child);
            }
            
            res.push_back(cur_level);
        }
        
        return res;
    }
};