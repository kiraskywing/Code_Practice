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
    vector<TreeNode*> generateTrees(int n) {
        return helper(1, n);
    }
    
    vector<TreeNode*> helper(int first, int last) {
        vector<TreeNode*> res;
        for (int i = first; i <= last; i++) {
            for (auto& left : helper(first, i - 1)) {
                for (auto& right : helper(i + 1, last)) {
                    TreeNode* node = new TreeNode(i);
                    node->left = left;
                    node->right = right;
                    res.push_back(node);
                }
            }
        }
        
        if (!res.empty())
            return res;
        else
            return {nullptr};
    }
};