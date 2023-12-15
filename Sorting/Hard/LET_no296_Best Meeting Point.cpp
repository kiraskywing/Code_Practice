class Solution {
public:
    int minTotalDistance(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<int> rows, cols;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    rows.push_back(i);
                    cols.push_back(j);
                }
            }
        }

        int row_mid = getMedian(rows), col_mid = getMedian(cols);
        int res = 0;
        for (int row : rows)
            res += abs(row - row_mid);
        for (int col : cols)
            res += abs(col - col_mid);
        return res;
    }

    int getMedian(vector<int>& items) {
        sort(items.begin(), items.end());
        int n = items.size();
        if (n % 2 == 1)
            return items[n / 2];
        return (items[n / 2 - 1] + items[n / 2]) / 2;
    }
};