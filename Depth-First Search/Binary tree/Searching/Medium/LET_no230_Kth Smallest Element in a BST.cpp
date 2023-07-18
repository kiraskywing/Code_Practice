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
    int kthSmallest(TreeNode* root, int k) {
        vector<TreeNode*> stack;
        while (root) {
            stack.push_back(root);
            root = root->left;
        }

        int res;
        TreeNode* cur;
        while (k-- > 0) {
            cur = stack.back();
            stack.pop_back();
            res = cur->val;
            if (cur->right) {
                cur = cur->right;
                while (cur) {
                    stack.push_back(cur);
                    cur = cur->left;
                }
            }
        }

        return res;
    }
};