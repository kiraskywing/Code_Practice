# The same as LeetCode no973. K Closest Points to Origin

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import heapq


class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """

    def kClosest(self, points, origin, k):
        self.heap = []

        for point in points:
            d = self.get_distance(point, origin)
            heapq.heappush(self.heap, (-d, -point.x, -point.y))

            if len(self.heap) > k:
                heapq.heappop(self.heap)

        result = []
        while len(self.heap) > 0:
            _, x, y = heapq.heappop(self.heap)
            result.append(Point(-x, -y))
        result.reverse()

        return result

    def get_distance(self, point, origin):
        return (point.x - origin.x) ** 2 + (point.y - origin.y) ** 2