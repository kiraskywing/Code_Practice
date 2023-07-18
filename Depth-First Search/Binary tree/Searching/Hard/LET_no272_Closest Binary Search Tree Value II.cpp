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
    vector<int> closestKValues(TreeNode* root, double target, int k) {
        vector<TreeNode*> lowers = buildStack(root, target);
        vector<TreeNode*> uppers(lowers);

        lowers.back()->val < target ? moveUppers(uppers) : moveLowers(lowers);

        vector<int> res;
        while (k-- > 0) {
            if (chooseLowers(lowers, uppers, target)) {
                res.push_back(lowers.back()->val);
                moveLowers(lowers);
            }
            else {
                res.push_back(uppers.back()->val);
                moveUppers(uppers);
            }
        }

        return res;
    }

private:
    vector<TreeNode*> buildStack(TreeNode* root, double target) {
        vector<TreeNode*> res;
        while (root) {
            res.push_back(root);
            root = target < root->val ? root->left : root->right;
        }
        return res;
    }

    void moveUppers(vector<TreeNode*>& stack) {
        TreeNode* cur = stack.back();
        if (cur->right) {
            cur = cur->right;
            while (cur) {
                stack.push_back(cur);
                cur = cur->left;
            }
        }
        else {
            stack.pop_back();
            while (!stack.empty() && stack.back()->right == cur) {
                cur = stack.back();
                stack.pop_back();
            }
        }
    }

    void moveLowers(vector<TreeNode*>& stack) {
        TreeNode* cur = stack.back();
        if (cur->left) {
            cur = cur->left;
            while (cur) {
                stack.push_back(cur);
                cur = cur->right;
            }
        }
        else {
            stack.pop_back();
            while (!stack.empty() && stack.back()->left == cur) {
                cur = stack.back();
                stack.pop_back();
            }
        }
    }

    bool chooseLowers(vector<TreeNode*>& lowers, vector<TreeNode*>& uppers, double target) {
        if (uppers.empty())
            return true;
        if (lowers.empty())
            return false;
        
        return target - lowers.back()->val < uppers.back()->val - target;
    }
};