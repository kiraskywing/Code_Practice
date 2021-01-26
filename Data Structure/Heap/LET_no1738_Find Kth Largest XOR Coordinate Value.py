class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        temp = []
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: dp[i][j] = matrix[i][j]
                elif i == 0: dp[i][j] = dp[i][j - 1] ^ matrix[i][j]
                elif j == 0: dp[i][j] = dp[i - 1][j] ^ matrix[i][j]
                else: dp[i][j] = (dp[i][j - 1] ^ dp[i - 1][j] ^ dp[i - 1][j - 1] ^ matrix[i][j])
                
                heapq.heappush(temp, dp[i][j])
                if len(temp) > k:
                    heapq.heappop(temp)
        
        return temp[0]