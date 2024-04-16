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
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        if (depth == 1)
            return new TreeNode(val, root, nullptr);

        queue<TreeNode*> q;
        q.push(root);

        while (depth-- > 2) {
            int n = q.size();
            while (n-- > 0) {
                TreeNode* cur = q.front();
                q.pop();
                if (cur->left) 
                    q.push(cur->left);
                if (cur->right) 
                    q.push(cur->right);
            }
        }

        TreeNode *cur;
        while (!q.empty()) {
            cur = q.front();
            q.pop();
            cur->left = new TreeNode(val, cur->left, nullptr);
            cur->right = new TreeNode(val, nullptr, cur->right);
        }

        return root;
    }
};