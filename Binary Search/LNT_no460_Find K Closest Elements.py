class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def kClosestNumbers(self, A, target, k):

        right = self.find_upper_closest(A, target)
        left = right - 1

        res = []

        for _ in range(k):

            if self.left_is_closer(A, target, left, right):
                res.append(A[left])
                left -= 1

            else:
                res.append(A[right])
                right += 1

        return res

    def find_upper_closest(self, nums, target):

        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end

        return end

    def left_is_closer(self, nums, target, left, right):

        if left < 0:
            return False
        if right >= len(nums):
            return True

        return target - nums[left] <= nums[right] - target
