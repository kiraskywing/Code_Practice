class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        dest = str([[1,2,3],[4,5,0]])
        queue = collections.deque([])
        m, n = 2, 3
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    queue.append((copy.deepcopy(board), i, j))
                    break
                    
        steps = 0
        visited = {str(board)}
        while queue:
            for _ in range(len(queue)):
                cur, i, j = queue.popleft()
                if str(cur) == dest:
                    return steps
                
                for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < m and 0 <= j2 < n:
                        cur[i][j], cur[i2][j2] = cur[i2][j2], cur[i][j]
                        key = str(cur)
                        if key not in visited:
                            visited.add(key)
                            queue.append((copy.deepcopy(cur), i2, j2))
                        cur[i][j], cur[i2][j2] = cur[i2][j2], cur[i][j]
            steps += 1
        
        return -1