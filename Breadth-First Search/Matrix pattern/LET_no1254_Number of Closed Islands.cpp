class Solution {
public:
    int closedIsland(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0)
                    res += isClosedIsland(grid, i, j) ? 1 : 0;
            }
        }
        return res;
    }

    int isClosedIsland(vector<vector<int>>& grid, int i_start, int j_start) {
        int m = grid.size(), n = grid[0].size();
        queue<pair<int, int>> q;
        q.push({i_start, j_start});
        grid[i_start][j_start] = 1;
        bool res = true;

        if (i_start == m - 1 || i_start == 0 || j_start == 0 || j_start == n - 1)
            res = false;

        int shift[4][2] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};

        while (!q.empty()) {
            int size = q.size();
            while (size > 0) {
                auto cur = q.front();
                q.pop();
                int i = cur.first, j = cur.second;

                for (int idx = 0; idx < 4; idx++) {
                    int i2 = i + shift[idx][0], j2 = j + shift[idx][1];
                    if (i == i2 && j == j2)
                        continue;

                    if (0 <= i2 && i2 < m && 0 <= j2 && j2 < n) {
                        if (grid[i2][j2] == 0) {
                            q.push({i2, j2});
                            grid[i2][j2] = 1;
                            if (i2 == m - 1 || i2 == 0 || j2 == 0 || j2 == n - 1)
                                res = false;
                        }
                    }
                }

                size--;
            }
        }

        return res;
    }
};