# The same as LeetCode no78. Subsets

class Solution:
    """
    @param nums: A set of Numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        nums.sort()
        result = []
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, start, path, result):
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i + 1, path, result)
            path.pop()
