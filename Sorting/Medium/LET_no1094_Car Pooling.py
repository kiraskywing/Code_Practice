class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        times = []
        for trip in trips:
            p, start, end = trip[0], trip[1], trip[2]
            times.append([start, p])
            times.append([end, -p])
        times.sort()
        for t in times:
            capacity -= t[1]
            if capacity < 0:
                return False
        return True