class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """

    def subarraySumII(self, A, start, end):
        n = len(A)
        small_sum, big_sum = 0, 0
        small_end, big_end = 0, 0
        result = 0

        for i in range(n):
            small_end = max(small_end, i)
            big_end = max(big_end, i)

            while small_end < n and small_sum + A[small_end] < start:
                small_sum += A[small_end]
                small_end += 1

            while big_end < n and big_sum + A[big_end] <= end:
                big_sum += A[big_end]
                big_end += 1

            result += big_end - small_end

            if i < small_end:
                small_sum -= A[i]
            if i < big_end:
                big_sum -= A[i]

        return result