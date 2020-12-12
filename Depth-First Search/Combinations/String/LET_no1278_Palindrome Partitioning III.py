class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        memo = {}
        return self.dfs(s, k, 0, memo)

    def dfs(self, string, k, index, memo):
        if (index, k) in memo:
            return memo[(index, k)]
        if len(string) - index == k:
            return 0
        if k == 1:
            return self.cost(string, index, len(string) - 1)

        result = float('inf')
        for index_2 in range(index + 1, len(string) - (k - 2)):
            result = min(result, self.dfs(string, k - 1, index_2, memo) + self.cost(string, index, index_2 - 1))
        memo[(index, k)] = result
        return result

    def cost(self, string, left, right):
        cost = 0
        while left < right:
            if string[left] != string[right]:
                cost += 1
            left += 1
            right -= 1
        return cost