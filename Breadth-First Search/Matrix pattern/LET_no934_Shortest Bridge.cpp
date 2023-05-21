vector<vector<int>> dir = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

class Solution {
public:
    int shortestBridge(vector<vector<int>>& grid) {
        queue<pair<int, int>> q;
        
        // paint one island to 2
        int m = grid.size(), n = grid[0].size();
        for (int i = 0; i < m && q.empty(); i++) {
            for (int j = 0; j < n && q.empty(); j++) {
                if (grid[i][j] == 1) {
                    paint(grid, i, j, q);
                    break;
                }
            }
        }

        while (!q.empty()) {
            pair<int, int> cur = q.front();
            q.pop();
            int i = cur.first, j = cur.second;
            for (int x = 0; x < 4; x++) {
                int i2 = i + dir[x][0], j2 = j + dir[x][1];
                if (0 <= i2 && i2 < m && 0 <= j2 && j2 < n) {
                    if (grid[i2][j2] == 1)
                        return grid[i][j] - 2;
                    else if (grid[i2][j2] == 0) {
                        grid[i2][j2] = grid[i][j] + 1;
                        q.push({i2, j2});
                    }
                }
            }
        }

        return 0;
    }

    void paint(vector<vector<int>>& grid, int i, int j, queue<pair<int, int>>& q) {
        int m = grid.size(), n = grid[0].size();

        if (!(0 <= i && i < m && 0 <= j && j < n && grid[i][j] == 1))
            return;

        grid[i][j] = 2;
        q.push({i, j});

        for (int x = 0; x < 4; x++)
            paint(grid, i + dir[x][0], j + dir[x][1], q);
    }
};