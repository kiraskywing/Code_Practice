class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        heap = [(0, start[0], start[1])]
        stopped_points = {(start[0], start[1]):0}
        
        while heap:
            dist, i, j = heapq.heappop(heap)
            if i == destination[0] and j == destination[1]:
                return dist
            
            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                i2, j2, d = i, j, 0
                while 0 <= i2 + di < m and 0 <= j2 + dj < n and maze[i2 + di][j2 + dj] != 1:
                    i2 += di
                    j2 += dj
                    d += 1
                if (i2, j2) not in stopped_points or dist + d < stopped_points[(i2, j2)]:
                    stopped_points[(i2, j2)] = dist + d
                    heapq.heappush(heap, (dist + d, i2, j2))
        
        return -1