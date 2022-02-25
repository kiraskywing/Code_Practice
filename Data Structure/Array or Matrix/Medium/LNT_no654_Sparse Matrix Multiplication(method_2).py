# The same as LeetCode no311. Sparse Matrix Multiplication

class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """

    def multiply(self, A, B):
        rows = self.convert_to_row_vectors(A)
        cols = self.convert_to_col_vectors(B)

        result = []
        for vector_r in rows:
            row = []
            for vector_c in cols:
                row.append(self.multiply_vectors(vector_r, vector_c))
            result.append(row)
        return result

    def convert_to_row_vectors(self, A):
        vectors = []
        for row in A:
            vector = []
            for col, val in enumerate(row):
                if val != 0:
                    vector.append((col, val))
            vectors.append(vector)
        return vectors

    def convert_to_col_vectors(self, B):
        n, m = len(B), len(B[0])
        vectors = []
        for j in range(m):
            vector = []
            for i in range(n):
                if B[i][j] != 0:
                    vector.append((i, B[i][j]))
            vectors.append(vector)
        return vectors

    def multiply_vectors(self, v1, v2):
        i, j, value = 0, 0, 0

        while i < len(v1) and j < len(v2):
            if v1[i][0] < v2[j][0]:
                i += 1
            elif v1[i][0] > v2[j][0]:
                j += 1
            else:
                value += v1[i][1] * v2[j][1]
                i += 1
                j += 1

        return value
