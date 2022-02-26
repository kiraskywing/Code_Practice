class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """

    def submatrixSum(self, matrix):
        if not matrix or not matrix[0]:
            return None

        n, m = len(matrix), len(matrix[0])
        for top in range(n):
            arr = [0] * m
            for down in range(top, n):
                prefix_hash = {0: -1}
                prefix_sum = 0
                for col in range(m):
                    arr[col] += matrix[down][col]
                    prefix_sum += arr[col]
                    if prefix_sum in prefix_hash:
                        return [(top, prefix_hash[prefix_sum] + 1), (down, col)]
                    prefix_hash[prefix_sum] = col

        return None