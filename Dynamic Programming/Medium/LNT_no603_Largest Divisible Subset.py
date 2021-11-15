# the same as LET_no368_Largest Divisible Subset

class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset
    """

    def largestDivisibleSubset(self, nums):
        length = len(nums)
        dp = [1] * length
        father_index = [-1] * length

        nums.sort()
        total_counts, index = 0, -1

        for i in range(length):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if 1 + dp[j] > dp[i]:
                        dp[i] = dp[j] + 1
                        father_index[i] = j
            if dp[i] >= total_counts:
                total_counts = dp[i]
                index = i

        result = []
        for i in range(total_counts):
            result.append(nums[index])
            index = father_index[index]

        return result
