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
    int closestValue(TreeNode* root, double target) {
        TreeNode *lower = root, *upper = root;
        
        while (root) {
            if (root->val > target) {
                upper = root;
                root = root->left;
            }
            else if (root->val < target) {
                lower = root;
                root = root->right;
            }
            else 
                return root->val;
        }
        
        return abs(upper->val - target) < abs(lower->val - target) ? upper->val : lower->val;
    }
};