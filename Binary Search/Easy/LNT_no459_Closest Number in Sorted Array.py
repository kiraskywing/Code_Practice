class Solution:
    """
    @param A: an integer array sorted in ascending order
    @param target: An integer
    @return: an integer
    """

    def closestNumber(self, A, target):
        if not A:
            return -1

        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] < target:
                left = mid
            elif A[mid] > target:
                right = mid
            else:
                return mid

        diff_left, diff_right = abs(target - A[left]), abs(target - A[right])
        if diff_left < diff_right:
            return left
        else:
            return right