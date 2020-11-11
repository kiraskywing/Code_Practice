class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        for i in range(m):
            left, right = 0, n - 1
            while left < n and right >= 0 and left <= right:
                if A[i][left] == A[i][right]:
                    A[i][left] = A[i][right] = A[i][left] ^ 1
                left += 1
                right -= 1
        return A