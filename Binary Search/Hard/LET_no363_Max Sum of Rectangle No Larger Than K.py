class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def maxSumSubarray(arr):
            res = float('-inf')
            cur = 0
            prefixSums = [float('inf')]
            for x in arr:
                bisect.insort(prefixSums, cur)
                cur += x
                i = bisect.bisect_left(prefixSums, cur - k)
                res = max(res, cur - prefixSums[i])
            return res
        
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n - 1):
                matrix[i][j + 1] += matrix[i][j]
        res = float('-inf')
        for j1 in range(n):
            for j2 in range(j1, n):
                arr = [matrix[i][j2] - (matrix[i][j1 - 1] if j1 > 0 else 0) for i in range(m)]
                res = max(res, maxSumSubarray(arr))
        
        return res