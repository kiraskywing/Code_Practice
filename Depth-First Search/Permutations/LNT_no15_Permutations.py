class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):

        result = []
        visited = [False] * len(nums)
        self.dfs(nums, visited, [], result)
        return result

    def dfs(self, nums, visited, temp, result):
        if len(temp) == len(nums):
            result.append(temp[:])
            return

        for i in range(len(nums)):
            if visited[i]:
                continue

            visited[i] = True
            temp.append(nums[i])
            self.dfs(nums, visited, temp, result)
            temp.pop()
            visited[i] = False