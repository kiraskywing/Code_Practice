class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def moves(x, y):
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < n and 0 <= y2 < n:
                    yield (x2, y2)
        def bfs(x, y, index):
            res = 1
            queue = collections.deque([(x, y)])
            grid[x][y] = index
            
            while queue:
                i, j = queue.popleft()
                for i2, j2 in moves(i, j):
                    if grid[i2][j2] == 1:
                        grid[i2][j2] = index
                        res += 1
                        queue.append((i2, j2))
            
            return res
        
        record = {0: 0}
        index = 2
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    record[index] = bfs(i, j, index)
                    index += 1
        
        res = max(record.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    possibles = set(grid[i2][j2] for i2, j2 in moves(i, j))
                    res = max(res, sum(record[index] for index in possibles) + 1)
        
        return res