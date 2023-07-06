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
        if (!root)
            return "";
        
        queue<TreeNode*> q;
        q.push(root);
        ostringstream out;

        int count_nodes = 0;
        while (!q.empty()) {
            count_nodes++;
            TreeNode* cur = q.front();
            q.pop();
            out << (cur ? to_string(cur->val) : "#") << ' ';

            if (cur) {
                q.push(cur->left);
                q.push(cur->right);
            }
        }

        return out.str();
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data == "")
            return nullptr;
        
        cout << data << endl;
        istringstream in(data);
        string val;
        vector<TreeNode*> nodes;

        int count = 0;
        while (in) {
            in >> val;
            if (in)
                nodes.push_back((val == "#" ? nullptr : new TreeNode(stoi(val))));
        }

        int cur = 0, fast = 1, n = nodes.size(), left, right;
        while (fast < n) {
            while (!nodes[cur])
                cur++;

            left = fast;
            right = fast + 1;
            nodes[cur]->left = nodes[left];
            nodes[cur]->right = nodes[right];
            cur++;
            fast += 2;
        }

        return nodes[0];
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec2 {
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