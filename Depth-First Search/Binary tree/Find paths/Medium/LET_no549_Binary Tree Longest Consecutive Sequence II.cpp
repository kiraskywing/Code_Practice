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
    int longestConsecutive(TreeNode* root) {
        auto [incr, decr, res] = helper(root);
        return res;
    }

    tuple<int, int, int> helper(TreeNode* cur) {
        if (!cur)
            return {0, 0, 0};

        int incr = 1, decr = 1;
        auto [left_incr, left_decr, left_res] = helper(cur->left);
        auto [right_incr, right_decr, right_res] = helper(cur->right);

        if (cur->left) {
            incr = cur->left->val == cur->val + 1 ? left_incr + 1 : 1;
            decr = cur->left->val == cur->val - 1 ? left_decr + 1 : 1;
        }
        if (cur->right) {
            if (cur->right->val == cur->val + 1)
                incr = max(incr, right_incr + 1);
            if (cur->right->val == cur->val - 1)
                decr = max(decr, right_decr + 1);
        }

        return {incr, decr, max(incr + decr - 1, max(left_res, right_res))};
    }
};