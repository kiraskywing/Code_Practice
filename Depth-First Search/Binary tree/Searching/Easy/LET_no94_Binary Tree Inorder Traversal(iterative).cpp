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
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode*> s;
        while (root) {
            s.push(root);
            root = root->left;
        }

        vector<int> res;
        TreeNode* cur;
        while (!s.empty()) {
            cur = s.top();
            s.pop();
            res.push_back(cur->val);
            if (cur->right) {
                cur = cur->right;
                while (cur) {
                    s.push(cur);
                    cur = cur->left;
                }
            }
        }

        return res;
    }
};