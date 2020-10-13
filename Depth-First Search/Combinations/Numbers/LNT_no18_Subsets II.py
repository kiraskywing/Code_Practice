class Solution:
    """
    @param nums: A set of Numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):

        nums.sort()
        result = []
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, start, temp, result):
        result.append(temp[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            temp.append(nums[i])
            self.dfs(nums, i + 1, temp, result)
            temp.pop()
