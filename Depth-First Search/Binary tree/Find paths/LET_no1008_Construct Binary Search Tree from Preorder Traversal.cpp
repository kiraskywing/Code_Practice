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
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        int i = 0;
        return helper(preorder, i, INT_MAX);
    }
    
    TreeNode* helper(vector<int>& nums, int& i, int bound) {
        if (i == nums.size() || nums[i] > bound)
            return nullptr;
        
        TreeNode* root = new TreeNode(nums[i++]);
        root->left = helper(nums, i, root->val);
        root->right = helper(nums, i, bound);
        
        return root;
    }
};