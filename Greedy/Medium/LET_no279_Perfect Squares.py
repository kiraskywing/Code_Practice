class Solution:
    def numSquares(self, n: int) -> int:
        visited = [False] * (n + 1)
        squares = []
        for edge in range(1, int(n ** 0.5) + 1):
            square = edge * edge
            visited[square] = True
            squares.append(square)

        queue = collections.deque(squares)
        res = 1
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == n:
                    return res
                for square in squares:
                    nxt = cur + square
                    if nxt <= n and not visited[nxt]:
                        visited[nxt] = True
                        queue.append(nxt)
            res += 1
        
        return 0