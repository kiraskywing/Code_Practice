# the same as LeetCode no152. Maximum Product Subarray

class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """

    def maxProduct(self, nums):
        if not nums:
            return 0

        pre_max = pre_min = result = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(nums[i], pre_max * nums[i], pre_min * nums[i])
            cur_min = min(nums[i], pre_max * nums[i], pre_min * nums[i])
            result = max(result, cur_max)
            pre_max, pre_min = cur_max, cur_min

        return result
