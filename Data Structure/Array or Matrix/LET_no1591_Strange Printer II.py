class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0])
        pos = [[m, n, 0, 0] for _ in range(61)]
        colors = set()
        for i in range(m):
            for j in range(n):
                c = targetGrid[i][j]
                colors.add(c)
                pos[c][0], pos[c][1] = min(pos[c][0], i), min(pos[c][1], j)
                pos[c][2], pos[c][3] = max(pos[c][2], i), max(pos[c][3], j)
        
        while colors:
            colors2 = set()
            for c in colors:
                if not self.test(targetGrid, c, pos):
                    colors2.add(c)
            if len(colors2) == len(colors):
                return False
            colors = colors2
        
        return True
    
    
    def test(self, grid, c, pos):
        for i in range(pos[c][0], pos[c][2] + 1):
            for j in range(pos[c][1], pos[c][3] + 1):
                if grid[i][j] > 0 and grid[i][j] != c:
                    return False
        for i in range(pos[c][0], pos[c][2] + 1):
            for j in range(pos[c][1], pos[c][3] + 1):
                grid[i][j] = 0
        return True