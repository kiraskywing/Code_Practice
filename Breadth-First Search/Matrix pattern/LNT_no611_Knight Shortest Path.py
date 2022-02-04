"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        if not grid or not grid[0]:
            return -1
        
        steps = 0
        queue = collections.deque([(source.x, source.y)])
        grid[source.x][source.y] = 1
        m, n = len(grid), len(grid[0])
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i == destination.x and j == destination.y:
                    return steps
                
                for di, dj in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == 0:
                        queue.append((i2, j2))
                        grid[i2][j2] = 1
            
            steps += 1

        return -1