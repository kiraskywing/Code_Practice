class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """

    def shortestPath2(self, grid):
        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])
        if n == 0:
            return -1

        dp = [[sys.maxsize for _ in range(n)] for _ in range(m)]
        dp[0][0] = 0

        for j in range(n):
            for i in range(m):
                if grid[i][j]:
                    continue
                for di, dj in [(-1, -2), (1, -2), (-2, -1), (2, -1)]:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < m and 0 <= j2 < n and dp[i2][j2] != sys.maxsize:
                        dp[i][j] = min(dp[i][j], dp[i2][j2] + 1)

        if dp[-1][-1] == sys.maxsize:
            return -1
        return dp[-1][-1]
