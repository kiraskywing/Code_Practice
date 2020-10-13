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
        result = []
        island = set()
        father = dict()
        self.size = 0

        for pos in operators:
            x, y = pos.x, pos.y
            if (x, y) in island:
                result.append(self.size)
                continue

            island.add((x, y))
            father[(x, y)] = (x, y)
            self.size += 1

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x2, y2 = x + dx, y + dy
                if (x2, y2) in island:
                    self.union(father, (x, y), (x2, y2))

            result.append(self.size)

        return result

    def union(self, father, point_a, point_b):
        root_a = self.find_root(father, point_a)
        root_b = self.find_root(father, point_b)
        if root_a != root_b:
            father[root_b] = root_a
            self.size -= 1

    def find_root(self, father, point):
        path = []
        while point != father[point]:
            path.append(point)
            point = father[point]

        for p in path:
            father[p] = point

        return point
