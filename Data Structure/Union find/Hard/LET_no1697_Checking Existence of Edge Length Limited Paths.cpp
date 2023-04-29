class UnionFind {
private:
    vector<int> parent, rank;
public:
    UnionFind(int size) {
        parent.resize(size, 0);
        for (int i = 0; i < size; i++)
            parent[i] = i;
    }

    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);

        return parent[x];
    }

    void join(int x, int y) {
        int px = find(x), py = find(y);
        if (px != py)
            parent[px] = py;
    }
};

class Solution {
public:
    vector<bool> distanceLimitedPathsExist(int n, vector<vector<int>>& edgeList, vector<vector<int>>& queries) {
        UnionFind uf(n);

        for (int i = 0; i < queries.size(); i++)
            queries[i].push_back(i);

        sort(queries.begin(), queries.end(), [](auto& l, auto& r) { return l[2] < r[2]; } );
        sort(edgeList.begin(), edgeList.end(), [](auto& l, auto& r) { return l.back() < r.back(); } );

        int i = 0;
        vector<bool> res(queries.size(), false);
        for (vector<int>& q : queries) {
            while (i < edgeList.size() && edgeList[i][2] < q[2]) {
                uf.join(edgeList[i][0], edgeList[i][1]);
                i++;
            }

            res[q.back()] = uf.find(q[0]) == uf.find(q[1]);
        }

        return res;
    }
};