class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<int> row_ones(m, 0), col_ones(n, 0), row_zeros(m, 0), col_zeros(n, 0);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                row_ones[i] += grid[i][j] == 1;
                col_ones[j] += grid[i][j] == 1;
                row_zeros[i] += grid[i][j] == 0;
                col_zeros[j] += grid[i][j] == 0;
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++)
                grid[i][j] = row_ones[i] + col_ones[j] - row_zeros[i] - col_zeros[j];
        }

        return grid;
    }
};