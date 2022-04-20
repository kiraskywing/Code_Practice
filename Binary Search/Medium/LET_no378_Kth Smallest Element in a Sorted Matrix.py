class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_val, max_val = matrix[0][0], matrix[n - 1][n - 1]
        
        while min_val + 1 < max_val:
            mid = (min_val + max_val) // 2
            if self.count(matrix, mid) >= k:
                max_val = mid
            else:
                min_val = mid
        
        if self.count(matrix, min_val) >= k:
            return min_val
        return max_val
    
    def count(self, matrix, target):
        j = len(matrix) - 1
        res = 0
        for i in range(len(matrix)):
            while j >= 0 and matrix[i][j] > target:
                j -= 1
            res += j + 1
        return res