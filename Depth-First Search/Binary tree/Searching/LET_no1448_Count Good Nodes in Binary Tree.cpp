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
    int goodNodes(TreeNode* root) {
        return helper(root, INT_MIN);
    }
    
    int helper(TreeNode* root, int maxNum) {
        if (!root)
            return 0;
        
        int res = 0;
        maxNum = max(maxNum, root->val);
        res += (root->val >= maxNum) + helper(root->left, maxNum) + helper(root->right, maxNum);
        
        return res;
    }
};