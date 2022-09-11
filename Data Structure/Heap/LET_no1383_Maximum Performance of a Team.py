class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        res = 0
        sum_speed = 0
        heap = []
        
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            heapq.heappush(heap, s)
            sum_speed += s
            if len(heap) > k:
                sum_speed -= heapq.heappop(heap)
            res = max(res, sum_speed * e)
        
        return res % (10 ** 9 + 7)