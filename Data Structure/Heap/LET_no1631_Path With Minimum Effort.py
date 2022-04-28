class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        diff = [[float('inf')] * n for _ in range(m)]
        diff[0][0] = 0
        temp = [(0, 0, 0)]
        
        while temp:
            d, i, j = heapq.heappop(temp)
            if i == m - 1 and j == n - 1:
                return d
            
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                i2, j2 = i + di, j + dj
                if 0 <= i2 < m and 0 <= j2 < n:
                    d2 = max(d, abs(heights[i2][j2] - heights[i][j]))
                    if d2 < diff[i2][j2]:
                        diff[i2][j2] = d2
                        heapq.heappush(temp, (d2, i2, j2))