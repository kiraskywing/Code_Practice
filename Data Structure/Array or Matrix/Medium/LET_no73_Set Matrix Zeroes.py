class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Approach1: use hashmap to record the rows and columns need to be set as zeros
        # Approach2: use matrix[0] to record cols need to be set as zeros
        #            use matrix[i][0], 0 <= i < m, to record rows need to be set as zeros
        
        m, n = len(matrix), len(matrix[0])
        row0_is_zero = any(num == 0 for num in matrix[0])
        col0_is_zero = any(matrix[i][0] == 0 for i in range(m))
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                    
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == 0 and row0_is_zero or j == 0 and col0_is_zero:
                    matrix[i][j] = 0
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0