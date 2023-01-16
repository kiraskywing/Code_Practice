class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size();
        if (n == 0)
            return 0;

        vector<vector<int>> memo(n, vector<int>(n, 0));
        for (int left = n - 1; left >= 0; left--) {
            memo[left][left] = 1;
            for (int right = left + 1; right < n; right++) {
                if (s[left] == s[right])
                    memo[left][right] = memo[left + 1][right - 1] + 2;
                else 
                    memo[left][right] = max(memo[left + 1][right], memo[left][right - 1]);
            }
        }

        return memo[0][n - 1];
    }
};