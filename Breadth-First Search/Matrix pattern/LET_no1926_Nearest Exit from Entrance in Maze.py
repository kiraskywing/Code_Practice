class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        start_i, start_j = entrance
        queue = collections.deque([(start_i, start_j)])
        maze[start_i][start_j] = '+'
        
        steps = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if (i, j) != (start_i, start_j) and (i in (0, m - 1) or j in (0, n - 1)):
                    return steps
                
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < m and 0 <= j2 < n and maze[i2][j2] == '.':
                        maze[i2][j2] = '+'
                        queue.append((i2, j2))
            steps += 1
        
        return -1