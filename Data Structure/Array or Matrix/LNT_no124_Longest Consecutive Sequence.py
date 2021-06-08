# The same as LeetCode no128. Longest Consecutive Sequence

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

class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for i in nums:
            if i - 1 not in nums:
                j = i + 1
                while j in nums:
                    j += 1
                res = max(res, j - i)
        return res