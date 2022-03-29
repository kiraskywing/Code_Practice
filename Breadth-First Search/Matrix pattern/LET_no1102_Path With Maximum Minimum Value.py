class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        heap = [(-grid[0][0], 0, 0)]
        visited[0][0] = True
        
        while heap:
            val, i, j = heapq.heappop(heap)
            if i == m - 1 and j == n - 1:
                return -val
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                i2, j2 = i + di, j + dj
                if 0 <= i2 < m and 0 <= j2 < n and not visited[i2][j2]:
                    visited[i2][j2] = True
                    heapq.heappush(heap, (max(val, -grid[i2][j2]), i2, j2))
        
        return -1