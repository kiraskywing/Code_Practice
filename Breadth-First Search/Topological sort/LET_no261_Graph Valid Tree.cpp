class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if (n - 1 != edges.size())
            return false;

        unordered_map<int, vector<int>> next_hops;
        for (vector<int>& e : edges) {
            next_hops[e[0]].push_back(e[1]);
            next_hops[e[1]].push_back(e[0]);
        }

        unordered_set<int> visited({0});
        queue<int> q;
        q.push(0);

        while (!q.empty()) {
            int cur = q.front();
            q.pop();

            for (int next : next_hops[cur]) {
                if (!visited.count(next)) {
                    visited.insert(next);
                    q.push(next);
                }
            }
        }

        return visited.size() == n;
    }
};