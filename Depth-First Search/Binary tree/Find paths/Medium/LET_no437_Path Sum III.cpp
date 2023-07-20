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
    int res = 0;
public:
    int pathSum(TreeNode* root, int targetSum) {
        unordered_map<long, int> memo;
        memo[0] = 1;
        dfs(root, targetSum, memo, 0);
        return res;
    }

    void dfs(TreeNode* root, int targetSum, unordered_map<long, int>& memo, long pre_sum) {
        if (!root)
            return;
        
        pre_sum += root->val;
        res += memo[pre_sum - targetSum];
        memo[pre_sum]++;
        dfs(root->left, targetSum, memo, pre_sum);
        dfs(root->right, targetSum, memo, pre_sum);
        memo[pre_sum]--;
    }
};