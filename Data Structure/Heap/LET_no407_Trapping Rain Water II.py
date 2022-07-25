class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n - 1], i, n - 1))
            heightMap[i][0] = heightMap[i][n - 1] = float('inf')
        for j in range(1, n - 1):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m - 1][j], m - 1, j))
            heightMap[0][j] = heightMap[m - 1][j] = float('inf')
            
        res = 0    
        while heap:
            cur_height, i, j = heapq.heappop(heap)
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                i2, j2 = i + di, j + dj
                if 0 <= i2 < m and 0 <= j2 < n and heightMap[i2][j2] != float('inf'):
                    height = max(cur_height, heightMap[i2][j2])
                    res += height - heightMap[i2][j2]
                    heapq.heappush(heap, (height, i2, j2))
                    heightMap[i2][j2] = float('inf')
        
        return res