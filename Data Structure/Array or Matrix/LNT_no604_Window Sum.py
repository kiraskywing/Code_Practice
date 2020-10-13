class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        n = len(nums)
        if n == 0 or n < k:
            return []

        result = [sum(nums[:k])]
        for i in range(k, len(nums)):
            result.append(result[-1] - nums[i - k] + nums[i])

        return result