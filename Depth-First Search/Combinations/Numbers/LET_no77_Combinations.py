class Solution:
    """
    @param n: Given the range of Numbers
    @param k: Given the Numbers of combinations
    @return: All the combinations of k Numbers out of 1..n
    """

    def combine(self, n, k):

        result = []
        self.dfs(n, k, 1, 0, [], result)
        return result

    def dfs(self, n, k, start, used, temp, result):
        if used == k:
            result.append(temp[:])
            return

        for i in range(start, n + 1):
            temp.append(i)
            self.dfs(n, k, i + 1, used + 1, temp, result)
            temp.pop()
