class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, A, B):

        sol = []
        a, b = 0, 0

        while a < len(A) and b < len(B):

            if A[a] < B[b]:
                sol.append(A[a])
                a += 1
            else:
                sol.append(B[b])
                b += 1

        if a < len(A):
            sol.extend(A[a:])

        if b < len(B):
            sol.extend(B[b:])

        return sol