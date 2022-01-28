class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        i, j, lessEqual = m - 1, 0, 0
        while i >= 0 and j < n:
            if matrix[i][j] <= target:
                lessEqual += i + 1
                j += 1
            else:
                i -= 1
        i, j, greaterEqual = 0, n - 1, 0
        while i < m and j >= 0:
            if matrix[i][j] >= target:
                greaterEqual += m - i
                j -= 1
            else:
                i += 1
        
        return (lessEqual + greaterEqual) - m * n
