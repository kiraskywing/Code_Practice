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
    int countNodes(TreeNode* root) {
        int res = 0, h = getHeight(root);
        while (root) {
            if (getHeight(root->right) == h - 1) {
                res += 1 << h;
                root = root->right;
            }
            else {
                res += 1 << (h - 1);
                root = root->left;
            }
            h--;
        }
        return res;
    }
    int getHeight(TreeNode* root) {
        return !root ? -1 : 1 + getHeight(root->left);
    }
};