class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def totalOccurrence(self, A, target):
        if not A:
            return 0

        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] < target:
                left = mid
            else:
                right = mid

        if A[left] == target:
            head = left
        elif A[right] == target:
            head = right
        else:
            head = -1

        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] <= target:
                left = mid
            else:
                right = mid

        if A[right] == target:
            tail = right
        elif A[left] == target:
            tail = left
        else:
            tail = -1

        if head >= 0 and tail >= 0:
            return tail - head + 1
        else:
            return 0
