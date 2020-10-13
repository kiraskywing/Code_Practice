class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers(self, A):

        for right in range(1, len(A)):

            left = right
            while left - 1 >= 0 and A[left] < A[left - 1]:
                A[left - 1], A[left] = A[left], A[left - 1]
                left -= 1