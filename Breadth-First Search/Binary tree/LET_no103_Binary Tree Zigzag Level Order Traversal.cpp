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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> res;
        
        if (!root)
            return res;

        queue<TreeNode*> q;
        q.push(root);

        vector<int> temp;
        bool need_rev = false;
        while (!q.empty()) {
            int n = q.size();
            while (n-- > 0) {
                TreeNode* cur = q.front();
                q.pop();
                temp.push_back(cur->val);

                if (cur->left) q.push(cur->left);
                if (cur->right) q.push(cur->right);
            }

            if (need_rev)
                reverse(temp.begin(), temp.end());

            need_rev = !need_rev;
            res.push_back(temp);
            temp.clear();
        }

        return res;
    }
};