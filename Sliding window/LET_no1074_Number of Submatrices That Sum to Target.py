class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            for j in range(n - 1):
                row[j + 1] += row[j]
        
        res = 0
        for j1 in range(n):
            for j2 in range(j1, n):
                pre_sum = collections.defaultdict(int)
                pre_sum[0] = 1
                cur = 0
                for i in range(m):
                    cur += matrix[i][j2] - (matrix[i][j1 - 1] if j1 > 0 else 0)
                    res += pre_sum[cur - target]
                    pre_sum[cur] += 1
        
        return res