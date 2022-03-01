class Solution:
    def numSquares(self, n: int) -> int:
        visited = [False] * (n + 1)
        squares = []
        for i in range(1, int(n ** 0.5) + 1):
            squares.append(i * i)
            visited[i] = True
        queue = collections.deque(squares)
        
        res = 1
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == n:
                    return res
                for num in squares:
                    nxt = cur + num
                    if nxt <= n and not visited[nxt]:
                        visited[nxt] = True
                        queue.append(nxt)
                    elif nxt > n:
                        break
            res += 1