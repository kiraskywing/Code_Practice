class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        queue = collections.deque([])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        
        steps = 1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < m and 0 <= j2 < n and rooms[i2][j2] > steps:
                        rooms[i2][j2] = steps
                        queue.append((i2, j2))
            steps += 1