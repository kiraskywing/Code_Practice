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
    double res = 0.0;
public:
    double maximumAverageSubtree(TreeNode* root) {
        dfs(root);
        return res;
    }

    pair<int,int> dfs(TreeNode* root) {
        if (!root)
            return {0, 0};

        pair<int, int> left_res = dfs(root->left);
        pair<int, int> right_res = dfs(root->right);
        int sum = left_res.first + right_res.first+ root->val;
        int count = left_res.second + right_res.second + 1;
        
        res = max(res, double(sum) / count);
        
        return {sum, count};
    }
};