class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n % 2 != 0:
            return self.find_kth(A, 0, B, 0, n // 2 + 1)
        else:
            smaller = self.find_kth(A, 0, B, 0, n // 2)
            larger = self.find_kth(A, 0, B, 0, n // 2 + 1)
            return (smaller + larger) / 2

    def find_kth(self, A, i, B, j, k):
        if i == len(A):
            return B[j + k - 1]
        if j == len(B):
            return A[i + k - 1]
        if k == 1:
            return min(A[i + k - 1], B[j + k - 1])

        a = A[i + k // 2 - 1] if i + k // 2 <= len(A) else None
        b = B[j + k // 2 - 1] if j + k // 2 <= len(B) else None

        if b is None or (a is not None and a < b):
            return self.find_kth(A, i + k // 2, B, j, k - k // 2)
        return self.find_kth(A, i, B, j + k // 2, k - k // 2)