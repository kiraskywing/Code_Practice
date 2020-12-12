class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0

        time = 0
        for i in range(1, len(points)):
            x_diff = points[i][0] - points[i - 1][0]
            y_diff = points[i][1] - points[i - 1][1]
            time += max(abs(x_diff), abs(y_diff))

        return time