class Solution {
public:
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        unordered_map<int, vector<int>> graph;
        vector<int> colors(n + 1, -1);
        for (auto pair : dislikes) {
            int a = pair[0], b = pair[1];
            graph[a].push_back(b);
            graph[b].push_back(a);
        }

        for (int i = 1; i <= n; i++) {
            if (colors[i] == -1 && !bfs(colors, graph, i))
                return false;
        }

        return true;   
    }

    bool bfs(vector<int>& colors, unordered_map<int, vector<int>>& graph, int start) {
        queue<int> q;
        q.push(start);
        colors[start] = 0;

        while (!q.empty()) {
            int n = q.size();
            while (n > 0) {
                int cur = q.front();
                q.pop();
                for (int nxt : graph[cur]) {
                    if (colors[nxt] == colors[cur])
                        return false;
                    else if (colors[nxt] == -1) {
                        colors[nxt] = 1 - colors[cur];
                        q.push(nxt);
                    }
                }
                n--;
            }
        }

        return true;
    }
};