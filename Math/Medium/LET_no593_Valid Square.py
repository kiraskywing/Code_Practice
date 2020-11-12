class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        dist = collections.defaultdict(int)
        
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                dist[(points[j][0] - points[i][0]) ** 2 + (points[j][1] - points[i][1]) ** 2] += 1
        
        return len(dist) == 2 and 2 in dist.values() and 4 in dist.values()