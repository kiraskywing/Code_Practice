/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
private:
    bool p_found, q_found;
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        p_found = q_found = false;
        TreeNode* res = helper(root, p, q);
        return p_found && q_found ? res : nullptr;
    }

    TreeNode* helper(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root)
            return nullptr;

        TreeNode* left_res = helper(root->left, p, q);
        TreeNode* right_res = helper(root->right, p, q);
        
        if (root == p) {
            p_found = true;
            return root;
        }
        if (root == q) {
            q_found = true;
            return root;
        }

        return left_res == nullptr ? right_res : right_res == nullptr ? left_res : root;
    }
};