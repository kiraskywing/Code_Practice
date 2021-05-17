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
    int res = 0;
    int minCameraCover(TreeNode* root) {
        return (dfs(root) == "toBeCovered") + res;
    }
    string dfs(TreeNode* node) {
        if (!node)
            return "covered";
        
        string left = dfs(node->left), right = dfs(node->right);
        if (left == "toBeCovered" || right == "toBeCovered") {
            res++;
            return "covering";
        }
        return (left == "covering" || right == "covering" ? "covered" : "toBeCovered");
    }
};