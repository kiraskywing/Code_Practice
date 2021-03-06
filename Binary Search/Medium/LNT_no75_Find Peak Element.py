# The same as LeetCode no162. Find Peak Element

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):

        left, right = 0, len(A) - 1

        while left + 1 < right:

            mid = (left + right) // 2

            if A[mid - 1] < A[mid] and A[mid] > A[mid + 1]:
                return mid

            elif A[mid] > A[mid - 1]:
                left = mid

            elif A[mid] > A[mid + 1]:
                right = mid

            else:
                left = mid