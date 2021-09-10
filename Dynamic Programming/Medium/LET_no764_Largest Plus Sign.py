class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        dp = [[n] * n for _ in range(n)]
        for i, j in mines:
            dp[i][j] = 0
        
        for i in range(n):
            left = right = up = down = 0
            for j, k in zip(range(n), reversed(range(n))):
                left = left + 1 if dp[i][j] else 0
                dp[i][j] = min(dp[i][j], left)
                right = right + 1 if dp[i][k] else 0
                dp[i][k] = min(dp[i][k], right)
                up = up + 1 if dp[j][i] else 0
                dp[j][i] = min(dp[j][i], up)
                down = down + 1 if dp[k][i] else 0
                dp[k][i] = min(dp[k][i], down)
        
        return max(map(max, dp))