class Solution {
public:
    string stoneGameIII(vector<int>& stoneValue) {
        vector<int> dp(4);
        int n = stoneValue.size();
        for (int i = n - 1; i >= 0; i--) {
            dp[i % 4] = -1e9;
            for (int k = 0, sum = 0; k < 3 && i + k < n; k++) {
                sum += stoneValue[i + k];
                dp[i % 4] = max(dp[i % 4], sum - dp[(i + k + 1) % 4]);
            }
        }

        return (dp[0] == 0 ? "Tie" : (dp[0] > 0 ? "Alice" : "Bob"));
    }
};