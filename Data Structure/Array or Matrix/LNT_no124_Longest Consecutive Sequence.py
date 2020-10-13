class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """

    def longestConsecutive(self, num):
        nums = sorted(set(num))
        count = 1
        result = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1
            else:
                result = max(result, count)
                count = 1
        result = max(result, count)
        return result
