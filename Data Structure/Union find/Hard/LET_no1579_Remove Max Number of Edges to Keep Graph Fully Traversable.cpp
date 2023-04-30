class UnionFind {
private:
    vector<int> parent;
    int size;

public:
    UnionFind(int n) {
        size = n;
        parent.resize(n);
        for (int i = 0; i < n; i++)
            parent[i] = i;
    }

    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }

    bool unite(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py)
            return false;
        
        parent[px] = py;
        size--;
        return true;
    }

    bool isTraverseAll() { return size == 1; }
};

class Solution {
public:
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        sort(edges.begin(), edges.end(), [](vector<int>& a, vector<int>& b) { return a[0] > b[0]; });
        
        UnionFind uf_alice(n), uf_bob(n);
        int n_edge = 0;
        for (vector<int>& edge : edges) {
            int type = edge[0], u = edge[1] - 1, v = edge[2] - 1;
            if (type == 3)
                n_edge += (uf_alice.unite(u, v) | uf_bob.unite(u, v)); // use '|' to let both join be executed
            else if (type == 2)
                n_edge += uf_bob.unite(u, v);
            else
                n_edge += uf_alice.unite(u, v);
        }
        
        return uf_alice.isTraverseAll() && uf_bob.isTraverseAll() ? edges.size() - n_edge : -1;
    }
};