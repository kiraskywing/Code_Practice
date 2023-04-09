class Solution {
public:
    int largestPathValue(string colors, vector<vector<int>>& edges) {
        int n = colors.size();
        unordered_map<int, vector<int>> graph;
        vector<int> indegree(n, 0);

        for (vector<int>& e: edges) {
            graph[e[0]].push_back(e[1]);
            indegree[e[1]]++;
        }

        vector<vector<int>> color_freq(n, vector<int>(26, 0));
        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                q.push(i);
                color_freq[i][colors[i] - 'a'] = 1;
            }
        }

        int res = 0, seen = 0;
        while (!q.empty()) {
            int cur = q.front();
            q.pop();

            int cur_freq = color_freq[cur][colors[cur] - 'a'];
            res = max(res, cur_freq);
            seen++;

            for (int nxt: graph[cur]) {
                for (int c = 0; c < 26; c++)
                    color_freq[nxt][c] = max(color_freq[nxt][c], color_freq[cur][c] + (c == colors[nxt] - 'a'));

                indegree[nxt]--;
                if (indegree[nxt] == 0)
                    q.push(nxt);
            }
        }

        return seen == n ? res : -1;
    }
};