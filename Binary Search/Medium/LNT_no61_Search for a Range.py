class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        if not A:
            return [-1, -1]

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
            return [-1, -1]

        left, right = head, len(A) - 1
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
        return [head, tail]
