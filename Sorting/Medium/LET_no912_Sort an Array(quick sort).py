from random import randint

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):

        self.quicksorter(A, 0, len(A) - 1)

    def quicksorter(self, A, left, right):
        if left >= right:
            return

        i, j = left, right
        pivot = A[randint(i, j)]

        while i <= j:
            while i <= j and A[i] < pivot:
                i += 1

            while i <= j and pivot < A[j]:
                j -= 1

            if i <= j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1

        self.quicksorter(A, left, j)
        self.quicksorter(A, i, right)