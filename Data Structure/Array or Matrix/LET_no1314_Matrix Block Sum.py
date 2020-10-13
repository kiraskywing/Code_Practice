class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        rangeSum = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                rangeSum[i + 1][j + 1] = rangeSum[i + 1][j] + rangeSum[i][j + 1] - rangeSum[i][j] + mat[i][j]

        result = [[0] * (n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                i2, j2, i3, j3 = max(0, i - K), max(0, j - K), min(m, i + K + 1), min(n, j + K + 1)
                result[i][j] = rangeSum[i3][j3] - rangeSum[i2][j3] - rangeSum[i3][j2] + rangeSum[i2][j2]
        return result