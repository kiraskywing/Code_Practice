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
    
public:
    vector<TreeNode*> allPossibleFBT(int n) {
        unordered_map<int, vector<TreeNode*>> memo;
        return helper(n, memo);
    }

    vector<TreeNode*> helper(int n, unordered_map<int, vector<TreeNode*>>& memo) {
        vector<TreeNode*> res;
        if (n % 2 == 0) 
            return res;
        
        if (memo.count(n))
            return memo[n];

        if (n == 1) {
            TreeNode* cur = new TreeNode(0);
            res.push_back(cur);
            memo[1] = res;
            return res;
        }
        
        for (int i = 2; i <= n; i += 2) {
            vector<TreeNode*> left_res = helper(i - 1, memo);
            vector<TreeNode*> right_res = helper(n - i, memo);
            for (int j = 0; j < left_res.size(); j++) {
                for (int k = 0; k < right_res.size(); k++) {
                    TreeNode* cur = new TreeNode(0);
                    cur->left = left_res[j];
                    cur->right = right_res[k];
                    res.push_back(cur);
                }
            }
        }

        memo[n] = res;
        return res;
    }
};