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
    bool isValidBST(TreeNode* root) {
        vector<TreeNode*> stack;
        while (root) {
            stack.push_back(root);
            root = root->left;
        }

        TreeNode *pre = nullptr, *cur;
        while (!stack.empty()) {
            cur = stack.back();
            stack.pop_back();
            if (pre && pre->val >= cur->val)
                return false;

            pre = cur;
            if (cur->right) {
                cur = cur->right;
                while (cur) {
                    stack.push_back(cur);
                    cur = cur->left;
                }
            }
        }

        return true;
    }
};