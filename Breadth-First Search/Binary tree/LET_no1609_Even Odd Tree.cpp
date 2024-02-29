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
    bool isEvenOddTree(TreeNode* root) {
        queue<TreeNode*> nodes;
        nodes.push(root);
        
        int level = 0, preVal = 0;
        while (!nodes.empty()) {
            int n = nodes.size();
            for (int i = 0; i < n; i++) {
                TreeNode* cur = nodes.front();
                nodes.pop();
                if (level % 2 == 0 && cur->val % 2 != 1 || level % 2 != 0 && cur->val % 2 != 0)
                    return false;
                if (i > 0 && (level % 2 == 0 && cur->val <= preVal || level % 2 != 0 && cur->val >= preVal))
                    return false;
                
                if (cur->left)
                    nodes.push(cur->left);
                if (cur->right)
                    nodes.push(cur->right);
                preVal = cur->val;
            }
            level++;
        }

        return true;
    }
};