class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        memo = collections.Counter(tasks)
        heap = []
        for count in memo.values():
            heapq.heappush(heap, -count)   # max heap
            
        res = 0
        cycle = n + 1
        while heap:
            temp = []
            for _ in range(cycle):
                if heap:
                    temp.append(-heapq.heappop(heap) - 1)
            for count in temp:
                if count > 0:
                    heapq.heappush(heap, -count)
            res += cycle if heap else len(temp)
        
        return res