class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """

    def maxSubmatrix(self, matrix):
        if not matrix or len(matrix[0]) == 0:
            return 0

        result = 0
        for i in range(len(matrix)):
            range_sum = [0 for _ in range(len(matrix[0]))]
            for j in range(i, len(matrix)):
                for k in range(len(matrix[0])):
                    range_sum[k] += matrix[j][k]
                temp = self.max_subarray(range_sum)
                result = max(result, temp)

        return result

    def max_subarray(self, nums):
        max_sum, min_sum = -sys.maxsize, 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(prefix_sum, min_sum)

        return max_sum