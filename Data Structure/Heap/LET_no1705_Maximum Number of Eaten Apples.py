import heapq

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        res = i = 0
        n = len(apples)
        queue = []
        
        while i <= n or queue:
            if i < n and apples[i] > 0:
                heapq.heappush(queue, [i + days[i], apples[i]])
            while queue and (queue[0][0] <= i or queue[0][1] == 0):
                heapq.heappop(queue)
            if queue:
                queue[0][1] -= 1
                res += 1
            i += 1
        
        return res