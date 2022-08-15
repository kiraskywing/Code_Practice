class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        i = j = 0
        di, dj = 0, 1
        
        for cur in range(1, n * n + 1):
            res[i][j] = cur
            i2, j2 = i + di, j + dj
            if not (0 <= i2 < n) or not (0 <= j2 < n) or res[i2][j2] != 0:
                di, dj = dj, -di
            i += di
            j += dj
        
        return res
    