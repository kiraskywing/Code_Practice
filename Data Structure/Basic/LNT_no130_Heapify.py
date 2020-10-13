class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """

    def heapify(self, A):

        for i in range(len(A) // 2 - 1, -1, -1):
            while True:
                child = i * 2 + 1
                if child >= len(A):
                    break
                if child + 1 < len(A) and A[child] > A[child + 1]:
                    child += 1
                if A[i] > A[child]:
                    A[i], A[child] = A[child], A[i]
                    i = child
                else:
                    break