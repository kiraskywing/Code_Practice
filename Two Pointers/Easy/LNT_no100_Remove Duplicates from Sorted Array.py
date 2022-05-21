# The same as LeetCode no26. Remove Duplicates from Sorted Array

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    def removeDuplicates(self, nums):
        if not nums:
            return

        left = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        return left + 1
