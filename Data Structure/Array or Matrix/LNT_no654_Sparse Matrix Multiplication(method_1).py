class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """

    def multiply(self, A, B):
        n = len(A)
        m = len(A[0])
        l = len(B[0])

        result = [[0] * l for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if A[i][j] != 0:
                    for k in range(l):
                        if B[j][k] != 0:
                            result[i][k] += A[i][j] * B[j][k]

        return result
