class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        memo = {}
        used = [False] * len(bikes)
        return self.dfs(0, workers, bikes, used, memo)

    def dfs(self, i, workers, bikes, used, memo):
        if i == len(workers):
            return 0

        if (i, tuple(used)) not in memo:
            cur = float('inf')
            for j in range(len(bikes)):
                if not used[j]:
                    used[j] = True
                    cur = min(cur, self.get_dist(workers[i], bikes[j]) + self.dfs(i + 1, workers, bikes, used, memo))
                    used[j] = False
            memo[(i, tuple(used))] = cur
        
        return memo[(i, tuple(used))]

    def get_dist(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
        