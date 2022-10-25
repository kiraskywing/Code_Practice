class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        col_max = [max(matrix[i][j] for i in range(m)) for j in range(n)]
        row_min = [min(row) for row in matrix]
        res = []
        
        for i in range(m):
            for j in range(n):
                if row_min[i] == col_max[j]:
                    res.append(matrix[i][j])
                    break
        
        return res