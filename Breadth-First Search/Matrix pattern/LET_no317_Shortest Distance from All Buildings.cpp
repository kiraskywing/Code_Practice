class Solution {
private:
    int m, n;
    vector<vector<int>> shift;
public:
    int shortestDistance(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();
        shift = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        vector<vector<int>> dist(m, vector<int>(n, 0));
        vector<vector<int>> buildings(m, vector<int>(n, 0));
        int count = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    count++;
                    bfs(grid, dist, buildings, i, j);
                }
            }
        }

        int res = INT_MAX;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (buildings[i][j] == count)
                    res = min(res, dist[i][j]);
            }
        }

        return res == INT_MAX ? -1 : res;
    }

    void bfs(vector<vector<int>>& grid, vector<vector<int>>& dist, vector<vector<int>>& buildings, int i, int j) {
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        queue<pair<int, int>> q;
        q.push({i, j});
        int d = 1, i2, j2;

        while (!q.empty()) {
            int times = q.size();
            while (times-- > 0) {
                i = q.front().first;
                j = q.front().second;
                q.pop();

                for (auto& s : shift) {
                    i2 = i + s[0];
                    j2 = j + s[1];
                    if (0 <= i2 && i2 < m && 0 <= j2 && j2 < n &&
                        grid[i2][j2] == 0 && !visited[i2][j2]) {
                        visited[i2][j2] = true;
                        buildings[i2][j2]++;
                        dist[i2][j2] += d;
                        q.push({i2, j2});
                    }
                }
            }

            d++;
        }
    }
};