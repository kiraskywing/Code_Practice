class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        res = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] += matrix[i - 1][j] if i > 0 and matrix[i][j] != 0 else 0
            nums = sorted(matrix[i], reverse=True)
            for i in range(len(nums)):
                res = max(res, nums[i] * (i + 1))
        
        return res