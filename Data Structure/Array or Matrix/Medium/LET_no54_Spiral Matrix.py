class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        i, j, di, dj = 0, 0, 0, 1
        m, n = len(matrix), len(matrix[0])
        
        for _ in range(m * n):
            res.append(matrix[i][j])
            matrix[i][j] = -1000
            if matrix[(i + di) % m][(j + dj) % n] == -1000:
                di, dj = dj, -di
            i, j = i + di, j + dj
        
        return res