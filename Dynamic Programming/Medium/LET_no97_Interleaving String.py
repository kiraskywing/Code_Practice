class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, k = map(len, (s1, s2, s3))
        if m + n != k:
            return False
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1] or dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
        
        return dp[m][n]