class Solution {
public:
    int orderOfLargestPlusSign(int n, vector<vector<int>>& mines) {
        vector<vector<int>> dp(n, vector<int>(n, n));
        for (auto& m : mines)
            dp[m[0]][m[1]] = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0, k = n - 1, left = 0, right = 0, up = 0, down = 0; j < n; j++, k--) {
                dp[i][j] = min(dp[i][j], left = (dp[i][j] ? left + 1 : 0));
                dp[i][k] = min(dp[i][k], right = (dp[i][k] ? right + 1 : 0));
                dp[j][i] = min(dp[j][i], up = (dp[j][i] ? up + 1 : 0));
                dp[k][i] = min(dp[k][i], down = (dp[k][i] ? down + 1 : 0));
            }
        }
        
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                res = max(res, dp[i][j]);
        }
        return res;
    }
};