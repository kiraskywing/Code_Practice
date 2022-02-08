# The same as LeetCode no305. Number of Islands II

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        label = 1
        self.size = 0
        grid = [[0 for _ in range(m)] for _ in range(n)]
        res = []
        parent = dict()
        
        for p in operators:
            i, j = p.x, p.y
            if grid[i][j] != 0:
                res.append(self.size)
                continue
            
            grid[i][j] = label
            parent[label] = label
            self.size += 1
            
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                i2, j2 = i + di, j + dj
                if 0 <= i2 < n and 0 <= j2 < m:
                    if grid[i2][j2] != 0:
                        self.union(parent, grid[i2][j2], label)
            
            label += 1
            res.append(self.size)
        
        return res
    
    def find(self, parent, i):
        if i != parent[i]:
            parent[i] = self.find(parent, parent[i])
        return parent[i]
    
    def union(self, parent, i, j):
        pi, pj = self.find(parent, i), self.find(parent, j)
        if pi != pj:
            parent[pj] = pi
            self.size -= 1
