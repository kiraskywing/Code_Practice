// The same as LintCode no1172_Binary Tree Tilt

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
     * @param root: the root
     * @return: the tilt of the whole tree
     */
    int res = 0;
    int findTilt(TreeNode * root) {
        // Write your code here
        dfs(root);
        return res;
    }
    int dfs(TreeNode* root) {
        if (!root)
            return 0;
        
        int leftSum = dfs(root->left);
        int rightSum = dfs(root->right);
        res += abs(leftSum - rightSum);

        return leftSum + rightSum + root->val;
    }
};