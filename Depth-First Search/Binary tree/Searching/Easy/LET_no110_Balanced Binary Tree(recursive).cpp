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
    bool isBalanced(TreeNode* root) {
        return getHeight(root) != -1;
    }

    int getHeight(TreeNode* root) {
        if (root == nullptr)
            return 0;
        
        int left_h = getHeight(root->left);
        int right_h = getHeight(root->right);
        if (left_h == -1 || right_h == -1 || abs(left_h - right_h) > 1)
            return -1;

        return max(left_h, right_h) + 1;
    }
};