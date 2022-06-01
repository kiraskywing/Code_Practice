class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        queue_f = collections.deque([(0, 0, 0)])
        visited_f = {(0, 0):0}
        queue_b = collections.deque([(x, y, 0)])
        visited_b = {(x, y):0}
        
        while queue_f or queue_b:
            if queue_f:
                i, j, steps = queue_f.popleft()
                if (i, j) in visited_b:
                    return steps + visited_b[(i, j)]
                self.move(queue_f, i, j, steps, visited_f)
            if queue_b:
                i, j, steps = queue_b.popleft()
                if (i, j) in visited_f:
                    return steps + visited_f[(i, j)]
                self.move(queue_b, i, j, steps, visited_b)
        
        return -1
    
    def move(self, queue, i, j, steps, visited):
        for di, dj in [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]:
            i2, j2 = i + di, j + dj
            if (i2, j2) not in visited:
                visited[(i2, j2)] = steps + 1
                queue.append((i2, j2, steps + 1))