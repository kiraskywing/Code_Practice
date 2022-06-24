class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        target = [-num for num in target]
        heapq.heapify(target)
        
        while True:
            cur = -heapq.heappop(target)
            total -= cur
            if cur == 1 or total == 1:
                return True
            if cur < total or total == 0 or cur % total == 0:
                return False
            cur %= total
            total += cur
            heapq.heappush(target, -cur)