class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        p, q, u, v = coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1]

        for x, y in coordinates:
            if (x - p) * (y - v) != (y - q) * (x - u):
                return False

        return True