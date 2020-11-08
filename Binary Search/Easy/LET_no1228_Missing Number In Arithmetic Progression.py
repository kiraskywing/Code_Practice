class Solution:
    def missingNumber(self, arr: List[int]) -> int:

        steps = len(arr)
        d = (arr[-1] - arr[0]) // steps

        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] == arr[0] + d * mid:
                left = mid + 1
            else:
                right = mid

        return arr[0] + d * left

        """
        return ((arr[-1] + arr[0]) * (len(arr) + 1) // 2 - sum(arr))
        """

        """
        if len(arr) < 3:
            return

        L, R = 1, len(arr) - 2

        diff_L = arr[L] - arr[L - 1]
        diff_R = arr[R + 1] - arr[R]

        if diff_L != diff_R:
            if arr[L - 1] + diff_R * 2 == arr[L]:
                return arr[L - 1] + diff_R
            else:
                return arr[R] + diff_L

        diff = diff_L

        while L <= R and arr[L] - arr[L - 1] == diff:
            L += 1
        while L <= R and arr[R + 1] - arr[R] == diff:
            R -= 1

        if arr[L - 1] + diff * 2 == arr[L]:
            return arr[L - 1] + diff
        if arr[R] + diff * 2 == arr[R + 1]:
            return arr[R] + diff

        return
        """