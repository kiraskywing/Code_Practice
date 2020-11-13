# The same as Leetcode no47_Permutations II

class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):

        nums.sort()
        visited = [False] * len(nums)
        result = []
        self.dfs(nums, visited, [], result)
        return result

    def dfs(self, nums, visited, permutation, result):
        if len(permutation) == len(nums):
            result.append(permutation[:])
            return

        for i in range(len(nums)):

            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue

            visited[i] = True
            permutation.append(nums[i])
            self.dfs(nums, visited, permutation, result)
            permutation.pop()
            visited[i] = False