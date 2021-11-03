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
    int res;
public:
    int sumNumbers(TreeNode* root) {
        res = 0;
        dfs(root, 0);
        return res;
    }
    
    void dfs(TreeNode* root, int cur) {
        if (!root)
            return;
        
        cur = cur * 10 + root->val;
        if (!root->left && !root->right)
            res += cur;
        dfs(root->left, cur);
        dfs(root->right, cur);
    }
};