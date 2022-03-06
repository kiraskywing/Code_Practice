# The same as LintCode no1225. Island Perimeter

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        queue = collections.deque([])
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    queue.append((i, j))
                    grid[i][j] = -1
                    break
        
        res = 0
        while queue:
            i, j = queue.popleft()
            
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                i2, j2 = i + di, j + dj
                if not (0 <= i2 < m and 0 <= j2 < n):
                    res += 1
                else:
                    if grid[i2][j2] == 0:
                        res += 1
                    elif grid[i2][j2] == 1:
                        queue.append((i2, j2))
                        grid[i2][j2] = -1
        
        return res