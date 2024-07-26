class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        memo = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            memo[i][i] = 0
        for i, j, weight in edges:
            memo[i][j] = memo[j][i] = weight

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    memo[i][j] = min(memo[i][j], memo[i][k] + memo[k][j])

        res = dict()
        for i in range(n):
            res[sum(d <= distanceThreshold for d in memo[i])] = i
        
        return res[min(res)]