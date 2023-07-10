class UnionFind {
private:
    int count, m, n;
    vector<int> parent;
public:
    UnionFind(int m, int n) { 
        count = 0;
        this->m = m;
        this->n = n;
        parent.resize(m * n, -1);
    }
    
    bool hasParent(int i, int j) {
        int idx = i * n + j;
        return parent[idx] != -1;
    }

    void add(int i, int j) {
        int idx = i * n + j;
        parent[idx] = idx;
        count++;
    }

    int getParent(int i, int j) {
        int idx = i * n + j;

        if (parent[idx] != idx) {
            i = parent[idx] / n;
            j = parent[idx] % n;
            parent[idx] = getParent(i, j);
        }

        return parent[idx];
    }

    void unite(int i, int j, int i2, int j2) {
        int p1 = getParent(i, j);
        int p2 = getParent(i2, j2);
        if (p1 != p2) {
            count--;
            parent[p1] = p2;
        }
    }

    int getCount() { return count; }
};

class Solution {
public:
    vector<int> numIslands2(int m, int n, vector<vector<int>>& positions) {
        UnionFind uf(m, n);
        vector<int> res;
        vector<vector<int>> shift = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        int i, j, i2, j2;

        for (auto& pos : positions) {
            i = pos[0];
            j = pos[1];
            if (!uf.hasParent(i, j)) {
                uf.add(i, j);
                for (auto& s : shift) {
                    i2 = i + s[0];
                    j2 = j + s[1];
                    if (0 <= i2 && i2 < m && 0 <= j2 && j2 < n && uf.hasParent(i2, j2))
                        uf.unite(i, j, i2, j2);
                }
            }

            res.push_back(uf.getCount());
        }

        return res;
    }
};