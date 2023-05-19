class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> nodes(n, 0);

        for (int i = 0; i < n; i++) {
            if (nodes[i] != 0)
                continue;

            nodes[i] = 1;
            queue<int> q;
            q.push(i);

            while (!q.empty()) {
                int u = q.front();
                q.pop();

                for (int v : graph[u]) {
                    if (nodes[v] == 0) {
                        nodes[v] = -nodes[u];
                        q.push(v);
                    }
                    else if (nodes[v] != -nodes[u])
                        return false;
                }
            }
        }

        return true;
    }
};

// A graph is bipartite if and only if the two ends of each edge have different colors.