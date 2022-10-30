class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = collections.deque([(0, 0, k)])
        visited = {(0, 0, k)}
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                i, j, k = queue.popleft()
                if i == m - 1 and j == n - 1:
                    return steps
                
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < m and 0 <= j2 < n:
                        if grid[i2][j2] == 0 and (i2, j2, k) not in visited:
                            visited.add((i2, j2, k))
                            queue.append((i2, j2, k))
                        elif grid[i2][j2] == 1 and k > 0 and (i2, j2, k - 1) not in visited:
                            visited.add((i2, j2, k - 1))
                            queue.append((i2, j2, k - 1))
            steps += 1
        
        return -1