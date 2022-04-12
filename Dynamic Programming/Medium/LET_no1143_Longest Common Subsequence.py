class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i, c in enumerate(text1, 1):
            for j, d in enumerate(text2, 1):
                dp[i][j] = max(dp[i - 1][j - 1] + (1 if c == d else 0), dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]

class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(2)]
        prev, cur = 0, 1
        for c in text1:
            prev, cur = cur, prev
            for j, d in enumerate(text2, 1):
                dp[cur][j] = max(dp[prev][j], dp[cur][j - 1], dp[prev][j - 1] + (1 if c == d else 0))
        
        return dp[cur][-1]

class Solution3:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = map(len, (text1, text2))
        if m < n:
            return self.longestCommonSubsequence(text2, text1)
        dp = [0] * (n + 1)
        for c in text1:
            prev1, prev2 = 0, 0
            for i, d in enumerate(text2, 1):
                prev1, prev2 = dp[i], prev1
                dp[i] = prev2 + 1 if c == d else max(prev1, dp[i - 1])
        
        return dp[-1]