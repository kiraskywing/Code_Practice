class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum(self, nums):
        prefix_memo = {0: -1}
        prefix_sum = 0

        for i, val in enumerate(nums):
            prefix_sum += val
            if prefix_sum not in prefix_memo:
                prefix_memo[prefix_sum] = i
            else:
                return [prefix_memo[prefix_sum] + 1, i]

        return [-1, -1]