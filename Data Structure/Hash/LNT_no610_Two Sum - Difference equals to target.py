class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum7(self, nums, target):
        memo = {}

        for i in range(len(nums)):
            if target + nums[i] in memo:
                return (memo[target + nums[i]] + 1, i + 1)
            elif nums[i] - target in memo:
                return (memo[nums[i] - target] + 1, i + 1)
            else:
                memo[nums[i]] = i

        return []