class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if not m:
            return 0
        n = len(matrix[0])
        left, right, height = [0] * n, [n] * n, [0] * n
        res = 0
        
        for i in range(m):
            curLeft, curRight = 0, n
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], curLeft)
                    height[j] += 1
                else:
                    left[j] = 0
                    curLeft = j + 1
                    height[j] = 0
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], curRight)
                    res = max(res, (right[j] - left[j]) * height[j])
                else:
                    right[j] = n
                    curRight = j
        
        return res