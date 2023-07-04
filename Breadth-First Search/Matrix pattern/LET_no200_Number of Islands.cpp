class Solution {
private:
    int count;
    int m, n;
    vector<pair<int, int>> shift;
public:
    int numIslands(vector<vector<char>>& grid) {
        count = 0;
        m = grid.size();
        n = grid[0].size();
        shift = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    bfs(grid, i, j);
                }
            }
        }

        return count;
    }

    void bfs(vector<vector<char>>& grid, int i, int j) {
        grid[i][j] = '0';
        queue<pair<int, int>> q;
        q.push({i, j});

        while (!q.empty()) {
            int i = q.front().first, j = q.front().second;
            q.pop();

            for (auto& d : shift) {
                int i2 = i + d.first, j2 = j + d.second;
                if (0 <= i2 && i2 < m && 0 <= j2 && j2 < n && grid[i2][j2] == '1') {
                    grid[i2][j2] = '0';
                    q.push({i2, j2});
                }
            }
        }
    }
};