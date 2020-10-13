class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        cols = len(matrix[0])
        start, end = 0, len(matrix) * cols - 1

        while start + 1 < end:
            mid = (start + end) // 2
            mid_i, mid_j = mid // cols, mid % cols
            if matrix[mid_i][mid_j] < target:
                start = mid
            elif matrix[mid_i][mid_j] > target:
                end = mid
            else:
                return True

        start_i, start_j = start // cols, start % cols
        end_i, end_j = end // cols, end % cols
        if matrix[start_i][start_j] == target:
            return True
        if matrix[end_i][end_j] == target:
            return True
        return False
