class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        cols = len(matrix[0])
        start, end = 0, len(matrix) * cols - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            i, j = mid // cols, mid % cols
            if target < matrix[i][j]: end = mid
            else: start = mid
        
        i, j = start // cols, start % cols
        if matrix[i][j] == target: return True
        i, j = end // cols, end % cols
        if matrix[i][j] == target: return True
        
        return False
