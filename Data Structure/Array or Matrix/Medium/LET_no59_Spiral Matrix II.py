class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        
        i, j, di, dj = 0, 0, 0, 1
        for cur in range(n * n):
            res[i][j] = cur + 1
            i += di
            j += dj
            if res[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
        
        return res