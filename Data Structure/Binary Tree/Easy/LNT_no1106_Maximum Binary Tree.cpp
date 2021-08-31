/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param nums: an array
     * @return: the maximum tree
     */
    TreeNode * constructMaximumBinaryTree(vector<int> &nums) {
        // Write your code here
        return helper(nums, 0, nums.size() - 1);
    }

    TreeNode* helper(vector<int>& nums, int left, int right) {
        if (left > right)
            return nullptr;
        
        int index = left, value = nums[left];
        for (int i = left; i <= right; i++) {
            if (nums[i] > value) {
                value = nums[i];
                index = i;
            }
        }

        TreeNode* node = new TreeNode(value);
        node->left = helper(nums, left, index - 1);
        node->right = helper(nums, index + 1, right);

        return node;
    }
};