import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dist = [[sys.maxsize] * n for _ in range(m)]
        minHeap = [(0, 0, 0)]
        
        while minHeap:
            d, r, c = heapq.heappop(minHeap)
            if r == m - 1 and c == n - 1:
                return d
            for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    newDist = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if newDist < dist[nr][nc]:
                        dist[nr][nc] = newDist
                        heapq.heappush(minHeap, (newDist, nr, nc))