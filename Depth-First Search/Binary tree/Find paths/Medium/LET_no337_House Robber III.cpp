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
    int rob(TreeNode* root) {
        int curLeft = 0, curRight = 0;
        return helper(root, curLeft, curRight);
    }
    
    int helper(TreeNode* cur, int& curLeft, int& curRight) {
        if (!cur)
            return 0;
            
        int leftLeft = 0, leftRight = 0, rightLeft = 0, rightRight = 0;
        curLeft = helper(cur->left, leftLeft, leftRight);
        curRight = helper(cur->right, rightLeft, rightRight);
        
        return max(cur->val + leftLeft + leftRight + rightLeft + rightRight, curLeft + curRight);
    }
};