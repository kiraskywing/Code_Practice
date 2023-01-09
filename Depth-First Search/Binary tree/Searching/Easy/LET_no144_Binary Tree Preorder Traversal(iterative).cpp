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
    vector<int> preorderTraversal(TreeNode* root) {
        if (!root)
            return {};

        vector<int> res;
        vector<TreeNode*> s;

        while (root) {
            res.push_back(root->val);
            s.push_back(root);
            root = root->left;
        }

        while (!s.empty()) {
            TreeNode* cur = s.back();
            s.pop_back();
            if (cur->right) {
                cur = cur->right;
                while (cur) {
                    res.push_back(cur->val);
                    s.push_back(cur);
                    cur = cur->left;
                }
            }
        }

        return res;
    }
};