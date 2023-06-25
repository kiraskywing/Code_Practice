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
    bool twoSumBSTs(TreeNode* root1, TreeNode* root2, int target) {
        if (!root1 || !root2)
            return false;
        
        vector<TreeNode*> stack_small, stack_large;
        TreeNode* small = nullptr;
        TreeNode* large = nullptr;
        
        while (true) {
            while (root1) {
                stack_small.push_back(root1);
                root1 = root1->left;
            }

            while (root2) {
                stack_large.push_back(root2);
                root2 = root2->right;
            }

            if (stack_small.empty() || stack_large.empty())
                break;

            small = stack_small.back();
            large = stack_large.back();
            int cur_val = small->val + large->val;

            if (cur_val == target)
                return true;
            else if (cur_val < target) {
                stack_small.pop_back();
                root1 = small->right;
            }
            else {
                stack_large.pop_back();
                root2 = large->left;
            }
        }

        return false;
    }
};