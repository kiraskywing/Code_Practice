class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers(self, A):

        for left in range(len(A) - 1):
            for right in range(len(A) - 1 - left):
                if A[right] > A[right + 1]:
                    A[right + 1], A[right] = A[right], A[right + 1]