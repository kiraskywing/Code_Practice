class Solution {
public:
    bool isValidSerialization(string preorder) {
        istringstream input(preorder);
        int slot = 1;
        string node;
        while (getline(input, node, ',')) {
            if (slot == 0)
                return false;
            slot = node == "#" ? slot - 1 : slot + 1;
        }
        return slot == 0;
    }
};