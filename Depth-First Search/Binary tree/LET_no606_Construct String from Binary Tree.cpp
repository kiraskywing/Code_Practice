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
    string tree2str(TreeNode* root) {
        string res;
        dfs(root, res);
        return res;
    }

    void dfs(TreeNode* cur, string& res) {
        if (!cur)
            return;
            
        res.append(to_string(cur->val));
        if (!cur->left && !cur->right)
            return;
        
        res.push_back('(');
        dfs(cur->left, res);
        res.push_back(')');

        if (cur->right) {
            res.push_back('(');
            dfs(cur->right, res);
            res.push_back(')');
        }
    }
};