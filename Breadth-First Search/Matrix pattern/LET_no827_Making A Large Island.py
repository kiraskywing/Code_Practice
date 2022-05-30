class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        memo = {0:0}
        ID = 2
        n = len(grid)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    memo[ID] = self.bfs(grid, i, j, n, ID)
                    ID += 1
        
        res = max(memo.values())
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    count = 1
                    visited = set()
                    for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        i2, j2 = i + di, j + dj
                        if 0 <= i2 < n and 0 <= j2 < n and grid[i2][j2] != 0:
                            ID = grid[i2][j2]
                            if ID not in visited:
                                visited.add(ID)
                                count += memo[ID]
                    res = max(res, count)
        
        return res
    
    def bfs(self, grid, i, j, n, ID):
        grid[i][j] = ID
        count = 1
        queue = collections.deque([(i, j)])
        
        while queue:
            i, j = queue.popleft()
            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                i2, j2 = i + di, j + dj
                if 0 <= i2 < n and 0 <= j2 < n and grid[i2][j2] == 1:
                    grid[i2][j2] = ID
                    queue.append((i2, j2))
                    count += 1
        
        return count