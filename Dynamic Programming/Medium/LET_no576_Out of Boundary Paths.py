class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        for move in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        i2, j2 = i + di, j + dj
                        if 0 <= i2 < m and 0 <= j2 < n:
                            dp[move][i][j] += dp[move - 1][i2][j2]
                        else:
                            dp[move][i][j] += 1
                    dp[move][i][j] %= (10 ** 9 + 7)
        
        return dp[maxMove][startRow][startColumn]

class Solution2:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        prev = [[0] * n for _ in range(m)]
        for move in range(1, maxMove + 1):
            cur = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        i2, j2 = i + di, j + dj
                        if 0 <= i2 < m and 0 <= j2 < n:
                            cur[i][j] += prev[i2][j2]
                        else:
                            cur[i][j] += 1
                    cur[i][j] %= (10 ** 9 + 7)
            prev = cur
        
        return prev[startRow][startColumn]