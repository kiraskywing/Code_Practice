# The same as LeetCode no304. Range Sum Query 2D - Immutable

class NumMatrix:
    """
    @param: matrix: a 2D matrix
    """

    def __init__(self, matrix):
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        if n == 0:
            return

        self.dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.dp[i + 1][j + 1] = self.dp[i][j + 1] + self.dp[i + 1][j] + matrix[i][j] - self.dp[i][j]

    """
    @param: row1: An integer
    @param: col1: An integer
    @param: row2: An integer
    @param: col2: An integer
    @return: An integer
    """

    def sumRegion(self, row1, col1, row2, col2):
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)