class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        
        heap = []    # (end, -prev_profit)
        max_profit = 0
        for start, end, cur_profit in jobs:
            while heap and heap[0][0] <= start:
                _, prev_profit = heapq.heappop(heap)
                max_profit = max(max_profit, -prev_profit)
                
            heapq.heappush(heap, (end, -(max_profit + cur_profit)))
            
        while heap:
            _, prev_profit = heapq.heappop(heap)
            max_profit = max(max_profit, -prev_profit)
        
        return max_profit
        