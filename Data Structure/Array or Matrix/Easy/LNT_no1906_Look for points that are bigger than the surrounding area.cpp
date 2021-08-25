class Solution {
public:
    /**
     * @param grid: a matrix
     * @return: Find all points that are strictly larger than their neighbors
     */
    vector<vector<int>> highpoints(vector<vector<int>> &grid) {
        // write your code here
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> res(m, vector<int>(n, 0)), dirs;
        for (int di = -1; di <= 1; di++) {
            for (int dj = -1; dj <= 1; dj++)
                dirs.emplace_back(vector<int>{di, dj});
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int check = 1;
                for (auto dir : dirs) {
                    int i2 = i + dir[0], j2 = j + dir[1];
                    if (0 <= i2 && i2 < m && 0 <= j2 && j2 < n && (i != i2 || j != j2) && grid[i][j] <= grid[i2][j2]) {
                        check = 0;
                        break;
                    }
                }
                res[i][j] = check;
            }
        }

        return res;
    }
};