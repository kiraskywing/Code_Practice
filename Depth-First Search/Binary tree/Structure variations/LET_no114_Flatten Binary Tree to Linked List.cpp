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
    TreeNode* lastNode; 
public:
    void flatten(TreeNode* root) {
        lastNode = nullptr;
        helper(root);
        return;
    }
    
    void helper(TreeNode* root) {
        if (!root) return;
        
        if (lastNode) {
            lastNode->left = nullptr;
            lastNode->right = root;
        }
        
        lastNode = root;
        TreeNode* right = root->right;
        helper(root->left);
        helper(right);
        
        return;
    }
};