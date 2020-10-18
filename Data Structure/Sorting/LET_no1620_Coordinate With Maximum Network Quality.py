import heapq

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        minheap = []
        for x in range(51):
            for y in range(51):
                quality = 0
                for i in range(len(towers)):
                    d = ((x - towers[i][0]) ** 2 + (y - towers[i][1]) ** 2) ** 0.5
                    if d <= radius:
                        quality += int(towers[i][2] / (1 + d))
                heapq.heappush(minheap, (-quality, x, y))
        
        return [minheap[0][1], minheap[0][2]]