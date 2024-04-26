class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        for (int i = 1; i < m; i++) {
            auto p = helper(grid[i - 1]);
            for (int j = 0; j < n; j++)
                grid[i][j] += (p.first == grid[i - 1][j] ? p.second : p.first);
        }

        auto p = helper(grid[m - 1]);
        return p.first;
    }

    pair<int, int> helper(vector<int>& arr) {
        int min = INT_MAX, min2 = INT_MAX;
        for (int num : arr) {
            if (num < min) {
                min2 = min;
                min = num;
            }
            else if (num < min2)
                min2 = num;
        }
        
        return {min, min2};
    }
};