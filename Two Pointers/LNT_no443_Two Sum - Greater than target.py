class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """

    def twoSum2(self, nums, target):
        n = len(nums)
        if n < 2:
            return 0

        nums.sort()
        left, right = 0, n - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] > target:
                count += right - left
                right -= 1
            else:
                left += 1

        return count
