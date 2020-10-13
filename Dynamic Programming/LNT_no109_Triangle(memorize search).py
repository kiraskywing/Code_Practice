class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        if not triangle or not triangle[0]:
            return -1

        self.triangle = triangle
        self.height = len(triangle)
        self.dp = [[sys.maxsize] * (i + 1) for i in range(self.height)]
        return self.search_min_in(0, 0)

    def search_min_in(self, x, y):
        if x >= len(self.triangle):
            return 0

        if self.dp[x][y] != sys.maxsize:
            return self.dp[x][y]

        self.dp[x][y] = min(self.search_min_in(x + 1, y), self.search_min_in(x + 1, y + 1)) + self.triangle[x][y]

        return self.dp[x][y]
