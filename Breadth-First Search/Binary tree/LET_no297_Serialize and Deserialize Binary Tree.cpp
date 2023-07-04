/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        ostringstream out;
        serialHelper(root, out);
        return out.str();
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream in(data);
        return deserialHelper(in);
    }

    void serialHelper(TreeNode* root, ostringstream& out) {
        if (root) {
            out << root->val << ' ';
            serialHelper(root->left, out);
            serialHelper(root->right, out);
        }
        else
            out << "# ";
    }

    TreeNode* deserialHelper(istringstream& in) {
        string val;
        in >> val;
        if (val == "#")
            return nullptr;

        TreeNode* cur = new TreeNode(stoi(val));
        cur->left = deserialHelper(in);
        cur->right = deserialHelper(in);
        return cur;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));