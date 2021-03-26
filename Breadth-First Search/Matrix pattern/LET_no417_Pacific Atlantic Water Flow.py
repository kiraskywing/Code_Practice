class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        
        m, n = len(matrix), len(matrix[0])
        pacific = set([(0, j) for j in range(n)] + [(i, 0) for i in range(1, m)])
        atlantic = set([(m - 1, j) for j in range(n)] + [(i, n - 1) for i in range(m - 1)])
        
        pacific = self.bfs(matrix, pacific, m, n)
        atlantic = self.bfs(matrix, atlantic, m, n)
        
        return list(pacific & atlantic)
    
    def bfs(self, matrix, visited, m, n):
        queue = collections.deque(visited)
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < m and 0 <= j2 < n and (i2, j2) not in visited and matrix[i2][j2] >= matrix[i][j]:
                        queue.append((i2, j2))
                        visited.add((i2, j2))
        return visited