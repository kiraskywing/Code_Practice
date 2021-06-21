class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq = [(grid[0][0], 0, 0)]
        seen = set([(0, 0)])
        res = 0
        
        while pq:
            cur, x, y = heapq.heappop(pq)
            res = max(cur, res)
            if x == y == n - 1:
                return res
            
            for x2, y2 in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= x2 < n and 0 <= y2 < n and (x2, y2) not in seen:
                    seen.add((x2, y2))
                    heapq.heappush(pq, (grid[x2][y2], x2, y2))