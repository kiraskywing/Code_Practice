/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isCousins(TreeNode* root, int x, int y) {
        int parent;
        queue<pair<TreeNode*, TreeNode*>> q;
        q.push(make_pair(nullptr, root));
        
        while (!q.empty()) {
            parent = 0;
            for (int i = q.size(); i > 0; i--) {
                auto cur = q.front(); q.pop();
                if (cur.first && (cur.second->val == x || cur.second->val == y)) {
                    if (!parent) 
                        parent = cur.first->val;
                    else 
                        return parent != cur.first->val;
                }
                
                if (cur.second->left) 
                    q.push(make_pair(cur.second, cur.second->left));
                if (cur.second->right) 
                    q.push(make_pair(cur.second, cur.second->right));
            }
        }
        return false;
    }
};