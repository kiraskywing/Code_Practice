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
private:
    unordered_map<int, int> table;
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        for (int i = 0; i < inorder.size(); i++)
            table[inorder[i]] = i;
        return helper(inorder, postorder, 0, inorder.size() - 1);
    }
    
    TreeNode* helper(vector<int>& in, vector<int>& post, int i_left, int i_right) {
        if (i_left > i_right)
            return nullptr;
        
        TreeNode* cur = new TreeNode(post.back());
        post.pop_back();
        int x = table[cur->val];
        
        cur->right = helper(in, post, x + 1, i_right);
        cur->left = helper(in, post, i_left, x - 1);
        
        return cur;
    }
};