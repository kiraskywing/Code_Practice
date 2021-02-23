class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        heights = [[-1] * n for _ in range(m)]
        queue = collections.deque([])
        
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    heights[i][j] = 0
                    queue.append((i, j))
        
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < m and 0 <= j2 < n and heights[i2][j2] == -1:
                        heights[i2][j2] = heights[i][j] + 1
                        queue.append((i2, j2))
        
        return heights