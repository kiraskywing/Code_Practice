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
        return helper(nullptr, root, 0);
    }
    int helper(TreeNode* parent, TreeNode* cur, int len) {
        if (!cur)
            return len;
        
        if (parent && parent->val + 1 == cur->val)
            len++;
        else
            len = 1;
        
        return max(len, max(helper(cur, cur->left, len), helper(cur, cur->right, len)));
    }
};