class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        for left in range(n - 1, -1, -1):
            for right in range(left, n):
                if s[left] == s[right]:
                    dp[left][right] = dp[left + 1][right - 1] if left + 1 <= right - 1 else True
                else:
                    dp[left][right] = False
        
        for i in range(1, n):
            for j in range(i, n - 1):
                if dp[0][i - 1] and dp[i][j] and dp[j + 1][n - 1]:
                    return True
        
        return False