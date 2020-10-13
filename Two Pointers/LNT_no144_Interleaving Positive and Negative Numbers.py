class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """

    def rerange(self, A):

        pos, neg = 0, 0
        for num in A:
            if num > 0:
                pos += 1
            else:
                neg += 1

        if pos >= neg:
            i, j = 0, 1
            while i < len(A) and j < len(A):
                if A[i] > 0 and A[j] < 0:
                    i += 2
                    j += 2
                elif A[i] > 0:
                    i += 2
                elif A[j] < 0:
                    j += 2
                else:
                    A[i], A[j] = A[j], A[i]
                    i += 2
                    j += 2

        else:
            i, j = 0, 1
            while i < len(A) and j < len(A):
                if A[i] < 0 and A[j] > 0:
                    i += 2
                    j += 2
                elif A[i] < 0:
                    i += 2
                elif A[j] > 0:
                    j += 2
                else:
                    A[i], A[j] = A[j], A[i]
                    i += 2
                    j += 2