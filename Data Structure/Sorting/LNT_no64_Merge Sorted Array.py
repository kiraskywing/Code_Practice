class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """

    def mergeSortedArray(self, A, m, B, n):

        while n > 0:

            if m == 0 or B[n - 1] > A[m - 1]:
                A[m + n - 1] = B[n - 1]
                n -= 1
            else:
                A[m + n - 1] = A[m - 1]
                m -= 1