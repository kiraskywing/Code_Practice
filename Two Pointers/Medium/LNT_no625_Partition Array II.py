class Solution:
    """
    @param nums: an integer array
    @param low: An integer
    @param high: An integer
    @return: nothing
    """

    def partition2(self, nums, low, high):

        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] < low:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] > high:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1