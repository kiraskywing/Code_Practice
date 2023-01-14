class UnionFind {
private:
    vector<int> mapping_char;
public:
    UnionFind() { 
        mapping_char.resize(26); 
        for (int i = 0; i < 26; i++)
            mapping_char[i] = i;
    }

    int find(int x) {
        int root = x;
        while (root != mapping_char[root])
            root = mapping_char[root];

        while (x != mapping_char[x]) {
            int temp = mapping_char[x];
            mapping_char[x] = root;
            x = temp;
        }

        return root;
    }

    void performUnion(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py)
            return;

        if (px < py)
            mapping_char[py] = px;
        else
            mapping_char[px] = py;
    }

};

class Solution {
public:
    string smallestEquivalentString(string s1, string s2, string baseStr) {
        UnionFind uf = UnionFind();

        for (int i = 0; i < s1.size(); i++)
            uf.performUnion(s1[i] - 'a', s2[i] - 'a');

        string res;
        for (char c : baseStr)
            res += (char) (uf.find(c - 'a') + 'a');
        return res;
    }
};