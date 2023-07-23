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
private:
    int res = INT_MIN;
public:
    int maxPathSum(TreeNode* root) {
        helper(root);
        return res;
    }

    int helper(TreeNode* cur) {
        if (!cur)
            return 0;

        int left_sum = helper(cur->left), right_sum = helper(cur->right);
        res = max(res, left_sum + right_sum + cur->val);
        return max(0, max(left_sum + cur->val, right_sum + cur->val));
    }
};