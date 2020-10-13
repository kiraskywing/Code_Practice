class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        max_length = 0
        dp = [[0 for _ in range(len(mat[0]) + 1)] for _ in range(len(mat) + 1)]

        for i in range(1, len(mat) + 1):
            for j in range(1, len(mat[0]) + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]

                left, right = 1, min(i, j)
                while left + 1 < right:
                    m = (left + right) // 2
                    cur_sum = dp[i][j] - dp[i - m][j] - dp[i][j - m] + dp[i - m][j - m]
                    if cur_sum <= threshold:
                        left = m
                    else:
                        right = m

                if dp[i][j] - dp[i - right][j] - dp[i][j - right] + dp[i - right][j - right] <= threshold:
                    max_length = max(max_length, right)
                elif dp[i][j] - dp[i - left][j] - dp[i][j - left] + dp[i - left][j - left] <= threshold:
                    max_length = max(max_length, left)

        return max_length