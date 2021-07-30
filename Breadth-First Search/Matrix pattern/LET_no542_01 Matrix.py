class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = collections.deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append([i, j])
                else:
                    mat[i][j] = float('inf')
        
        while queue:
            i, j = queue.popleft()
            for di, dj in ([1, 0], [0, 1], [-1, 0], [0, -1]):
                i2, j2 = i + di, j + dj
                if  not (0 <= i2 < m and 0 <= j2 < n) or mat[i2][j2] <= mat[i][j] + 1:
                    continue
                queue.append([i2, j2])
                mat[i2][j2] = mat[i][j] + 1
        
        return mat