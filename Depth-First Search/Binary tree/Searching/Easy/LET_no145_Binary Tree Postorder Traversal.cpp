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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        dfs(root, res);
        return res;
    }

    void dfs(TreeNode* root, vector<int>& res) {
        if (!root)
            return;

        dfs(root->left, res);
        dfs(root->right, res);
        res.push_back(root->val);
    }
};

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
class Solution2 {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<TreeNode*> stack;
        vector<int> res;

        while (root) {
            stack.push_back(root);
            root = root->left ? root->left : root->right;
        }

        TreeNode *cur;
        while (!stack.empty()) {
            cur = stack.back();
            stack.pop_back();
            res.push_back(cur->val);;

            if (!stack.empty() && stack.back()->left == cur) {
                cur = stack.back()->right;
                while (cur) {
                    stack.push_back(cur);
                    cur = cur->left ? cur->left : cur->right;
                }
            }
        }

        return res;
    }
};