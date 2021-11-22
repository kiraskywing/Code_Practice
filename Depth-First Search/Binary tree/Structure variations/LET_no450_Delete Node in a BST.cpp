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
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root)
            return nullptr;
        if (root->val == key) {
            if (!root->right) {
                TreeNode* nxt = root->left;
                delete root;
                return nxt;
            }
            else {
                TreeNode* nxt = root->right;
                while (nxt->left)
                    nxt = nxt->left;
                swap(nxt->val, root->val);
                root->right = deleteNode(root->right, key);
            }
            
        }
        else if (key < root->val)
            root->left = deleteNode(root->left, key);
        else
            root->right = deleteNode(root->right, key);
        
        return root;
    }
};