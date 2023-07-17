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
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
        if (!root)
            return res;

        string s = to_string(root->val);
        dfs(root, s, res);
        return res;
    }

    void dfs(TreeNode* root, string& s, vector<string>& res) {
        if (!root->left && !root->right) {
            res.push_back(s);
            return;
        }

        if (root->left) {
            s += "->" + to_string(root->left->val);
            dfs(root->left, s, res);
            size_t pos = s.rfind("->");
            s.erase(pos, s.size() - pos);
        }

        if (root->right) {
            s += "->" + to_string(root->right->val);
            dfs(root->right, s, res);
            size_t pos = s.rfind("->");
            s.erase(pos, s.size() - pos);
        }
    }
};