class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int, int>> q;
        int m = grid.size(), n = grid[0].size(), fresh = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2)
                    q.push({i, j});
                if (grid[i][j] == 1)
                    fresh++;
            }
        }
        
        int res = 0, i2, j2;
        int shifts[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        while (!q.empty()) {
            bool nxt = false;
            for (int i = q.size(); i > 0; i--) {
                auto p = q.front();
                q.pop();
                for (int j = 0; j < 4; j++) {
                    i2 = p.first + shifts[j][0];
                    j2 = p.second + shifts[j][1];
                    if (0 <= i2 && i2 < m && 0 <= j2 && j2 < n && grid[i2][j2] == 1) {
                        nxt = true;
                        grid[i2][j2] = 2;
                        fresh--;
                        q.push({i2, j2});
                    }
                }
            }
            res += nxt;
        }
        
        return fresh == 0 ? res : -1;
    }
};