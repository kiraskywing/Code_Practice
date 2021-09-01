# The same as LeetCode no.153. Find Minimum in Rotated Sorted Array

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin(self, nums):

        left, right = 0, len(nums) - 1
        target = nums[-1]

        while left + 1 < right:

            mid = (left + right) // 2

            if nums[mid] <= target:
                right = mid
            else:
                left = mid

        return min(nums[left], nums[right])