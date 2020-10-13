from random import randint


class Solution:
    """
    @param nums: an integer array
    @return: the maximum product
    """

    def maximumProduct(self, nums):

        if len(nums) < 3:
            return False

        self.quicksort(nums, 0, len(nums) - 1)

        return max(nums[-1] * nums[-2] * nums[-3], nums[-1] * nums[0] * nums[1])

    def quicksort(self, nums, left, right):

        if left >= right:
            return

        pivot = nums[randint(left, right)]
        i, j = left, right

        while i <= j:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        self.quicksort(nums, left, j)
        self.quicksort(nums, i, right)