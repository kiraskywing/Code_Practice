class UnionFind {
private:
    vector<int> parent;
public:
    UnionFind(int n): parent(n) {
        for (int i = 0; i < n; i++)
            parent[i] = i;
    }

    int find(int x) {
        int p = x;
        while (p != parent[p])
            p = parent[p];

        while (x != parent[x]) {
            int temp = parent[x];
            parent[x] = p;
            x = temp;
        }

        return p;
    }

    void connect(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py)
            return;

        parent[px] = py;
    }
};

class Solution {
public:
    int numberOfGoodPaths(vector<int>& vals, vector<vector<int>>& edges) {
        int n_nodes = vals.size();
        int res = n_nodes;
        
        map<int, vector<int>> same_value_nodes;
        for (int i = 0; i < n_nodes; i++)
            same_value_nodes[vals[i]].push_back(i);

        vector<vector<int>> adj_nodes(n_nodes);
        for (auto& e : edges) {
            int u = e[0], v = e[1];
            if (vals[u] >= vals[v])
                adj_nodes[u].push_back(v);
            else
                adj_nodes[v].push_back(u);
        }

        UnionFind uf(n_nodes);

        for (auto& [_, nodes] : same_value_nodes) {
            for (int u : nodes) {
                for (int v : adj_nodes[u]) {
                    uf.connect(u, v);
                }
            }

            unordered_map<int, int> group;
            for (int u : nodes)
                group[uf.find(u)]++;

            for (auto &[_, counts] : group)
                res += counts * (counts - 1) / 2;
            cout << res << endl;
        }

        return res;
    }
};