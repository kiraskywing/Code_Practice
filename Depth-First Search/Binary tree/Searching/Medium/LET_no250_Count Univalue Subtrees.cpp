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
    int count;
public:
    int countUnivalSubtrees(TreeNode* root) {
        count = 0;
        dfs(root);
        return count;
    }

    bool dfs(TreeNode* root) {
        if (!root)
            return true;
        
        bool left_is_uni = dfs(root->left), right_is_uni = dfs(root->right);
        if (left_is_uni && 
            right_is_uni && 
            (!root->left || root->left->val == root->val) &&
            (!root->right || root->right->val == root->val)) {
            count++;
            return true;
        }
        
        return false;
    }
};