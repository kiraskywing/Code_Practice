class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque([])
        m, n, fresh = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        
        res = 0
        while queue:
            nxt = False
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == 1:
                        nxt = True
                        grid[i2][j2] = 2
                        fresh -= 1
                        queue.append((i2, j2))
            if nxt: res += 1
        
        return res if fresh == 0 else -1