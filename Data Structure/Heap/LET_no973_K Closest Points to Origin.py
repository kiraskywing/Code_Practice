class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp = []
        for x, y in points:
            heapq.heappush(temp, (-(x ** 2 + y ** 2), x, y))
            if len(temp) > k:
                heapq.heappop(temp)
        return [[x, y] for _, x, y in temp]