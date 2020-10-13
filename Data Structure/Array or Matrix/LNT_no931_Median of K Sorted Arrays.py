class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """

    def findMedian(self, nums):
        if not nums:
            return 0.0

        n = sum(len(array) for array in nums)
        if n == 0:
            return 0.0

        if n % 2 != 0:
            return self.find_kth(nums, n // 2 + 1) * 1.0
        else:
            smaller = self.find_kth(nums, n // 2)
            larger = self.find_kth(nums, n // 2 + 1)
            return (smaller + larger) / 2.0

    def find_kth(self, arrs, k):
        min_val, max_val = self.get_range(arrs)

        while min_val + 1 < max_val:
            mid = (min_val + max_val) // 2
            if self.get_smaller_or_equal(arrs, mid) >= k:
                max_val = mid
            else:
                min_val = mid
        if self.get_smaller_or_equal(arrs, min_val) >= k:
            return min_val
        return max_val

    def get_range(self, arrs):
        min_val = min(i[0] for i in arrs if i)
        max_val = max(i[-1] for i in arrs if i)
        return min_val, max_val

    def get_smaller_or_equal(self, arrs, target):
        count = 0
        for i in arrs:
            if i:
                count += self.counter(i, target)
        return count

    def counter(self, arr, target):
        left, right = 0, len(arr) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] > target:
                right = mid
            else:
                left = mid

        if arr[left] > target:
            return left
        if arr[right] > target:
            return right
        return right + 1
