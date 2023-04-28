class UnionFind {
private:
    vector<int> parent;
    int n;

public:
    UnionFind(int size) {
        parent.resize(size);
        for (int i = 0; i < size; i++)
            parent[i] = i;
        n = size;
    }

    int find(int x) {
        int root = x;
        while (root != parent[root])
            root = parent[root];

        while (x != parent[x]) {
            int old_root = parent[x];
            parent[x] = root;
            x = old_root;
        }
        
        return root;
    }

    void join(int x, int y) {
        int px = find(x), py = find(y);
        if (px != py) {
            parent[px] = py;
            n--;
        }
    }

    int size() {
        return n;
    }
};

class Solution {
public:
    int numSimilarGroups(vector<string>& strs) {
        UnionFind uf(strs.size());
        for (int i = 0; i < strs.size(); i++) {
            for (int j = i + 1; j < strs.size(); j++) {
                if (isSimilar(strs[i], strs[j]))
                    uf.join(i, j);
            }
        }

        return uf.size();
    }

    bool isSimilar(string& a, string &b) {
        int diff = 0;
        for (int i = 0; i < a.size(); i++) {
            if (a[i] != b[i]) {
                diff++;
                if (diff > 2)
                    return false;
            }
        }

        return true;
    }
};