class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin(self, nums):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] == nums[end]:
                end -= 1
            else:
                start = mid

        if nums[start] < nums[end]:
            return nums[start]
        return nums[end]
