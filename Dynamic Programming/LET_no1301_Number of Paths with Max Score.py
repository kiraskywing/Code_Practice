class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        m, n = len(board), len(board[0])

        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        mod = 10 ** 9 + 7

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == "X":
                    dp[i][j] = [0, 0]
                    continue

                if i == m - 1 and j == n - 1:
                    dp[i][j] = [0, 1]
                    continue
                elif i == m - 1:
                    dp[i][j][0] = dp[i][j + 1][0]
                    dp[i][j][1] = dp[i][j + 1][1]
                elif j == n - 1:
                    dp[i][j][0] = dp[i + 1][j][0]
                    dp[i][j][1] = dp[i + 1][j][1]
                else:
                    for di, dj in [(1, 0), (0, 1), (1, 1)]:
                        i2, j2 = i + di, j + dj
                        if dp[i2][j2][0] > dp[i][j][0]:
                            dp[i][j] = [dp[i2][j2][0], 0]
                        if dp[i2][j2][0] == dp[i][j][0]:
                            dp[i][j][1] += dp[i2][j2][1]

                if dp[i][j][1] == 0:
                    dp[i][j][0] = 0
                    continue
                if i != 0 or j != 0:
                    dp[i][j][0] += int(board[i][j])

        return [dp[0][0][0], dp[0][0][1] % mod]