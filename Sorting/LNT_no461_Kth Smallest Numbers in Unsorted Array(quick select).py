from random import randint


class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """

    def kthSmallest(self, k, nums):
        return self.quickselect(nums, 0, len(nums) - 1, k - 1)

    def quickselect(self, nums, start, end, target):
        if start == end:
            return nums[start]

        left, right = start, end
        pivot = nums[randint(left, right)]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1;
                right -= 1

        if right >= target and right >= start:
            return self.quickselect(nums, start, right, target)
        elif target >= left and left <= end:
            return self.quickselect(nums, left, end, target)
        return nums[target]