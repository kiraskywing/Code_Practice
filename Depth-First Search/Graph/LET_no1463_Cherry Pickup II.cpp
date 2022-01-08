class Solution {
public:
    int dp[70][70][70];
    int cherryPickup(vector<vector<int>>& grid) {
        memset(dp, -1, sizeof(dp));
        int m = grid.size(), n = grid[0].size();
        return dfs(grid, m, n, 0, 0, n - 1);
    }
    
    int dfs(vector<vector<int>>& grid, int m, int n, int r, int c1, int c2) {
        if (dp[r][c1][c2] != -1)
            return dp[r][c1][c2];
        
        int res = 0;
        for (int d1 = -1; d1 <= 1; d1++) {
            for (int d2 = -1; d2 <= 1; d2++) {
                int c3 = c1 + d1, c4 = c2 + d2, r2 = r + 1;
                if (r2 < m && 0 <= c3 && c3 < n && 0 <= c4 && c4 < n)
                    res = max(res, dfs(grid, m, n, r2, c3, c4));
            }
        }
        
        res += c1 == c2 ? grid[r][c1] : grid[r][c1] + grid[r][c2];
        dp[r][c1][c2] = res;
        return res;
    }
};