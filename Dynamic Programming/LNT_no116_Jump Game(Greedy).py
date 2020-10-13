class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """

    def canJump(self, A):
        farthest = A[0]

        for i in range(1, len(A)):
            if i <= farthest and A[i] + i >= farthest:
                farthest = A[i] + i

        return farthest >= len(A) - 1
