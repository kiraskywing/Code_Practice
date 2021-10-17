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
    unordered_map<int, int> record;
    int res;
public:
    int pathSum(TreeNode* root, int targetSum) {
        record[0] = 1;
        res = 0;
        helper(root, targetSum, 0);
        return res;
    }
    void helper(TreeNode* root, int targetSum, int preSum) {
        if (!root)
            return;
        
        preSum += root->val;
        if (record.count(preSum - targetSum))
            res += record[preSum - targetSum];
        record[preSum] += 1;
        helper(root->left, targetSum, preSum);
        helper(root->right, targetSum, preSum);
        record[preSum] -= 1;
    }
};