class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n - 1):
                matrix[i][j + 1] += matrix[i][j]
                
        res = float('-inf')
        for j1 in range(n):
            for j2 in range(j1, n):
                window_sum = [matrix[i][j2] - (matrix[i][j1 - 1] if j1 > 0 else 0) for i in range(m)]
                res = max(res, self.getMaxSum(window_sum, k))
        
        return res
    
    def getMaxSum(self, arr, limit):
        res = float('-inf')
        cur = 0
        temp = [float('inf')]
        
        for num in arr:
            bisect.insort(temp, cur)    # find position: O(logn), insert: O(n)
            cur += num
            i = bisect.bisect_left(temp, cur - limit)
            res = max(res, cur - temp[i])
        
        return res