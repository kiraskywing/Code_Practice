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
    int rangeSumBST(TreeNode* root, int low, int high) {
        stack<TreeNode*> st;
        st.push(root);
        int res = 0;
        
        while (!st.empty()) {
            TreeNode* cur = st.top();
            st.pop();
            if (low <= cur->val && cur->val <= high)
                res += cur->val;
            
            if (cur->left)
                st.push(cur->left);
            if (cur->right)
                st.push(cur->right);
        }
        
        return res;
    }
};