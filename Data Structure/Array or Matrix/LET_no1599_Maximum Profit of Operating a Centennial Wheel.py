class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        run = max_run = 0
        prof = max_prof = 0
        cur = 0
        i = 0
        
        while cur > 0 or i < len(customers):
            if i < len(customers):
                cur += customers[i]
                i += 1
            temp = min(4, cur)
            cur -= temp
            prof += (boardingCost * temp - runningCost)
            run += 1
            if prof > max_prof:
                max_prof = prof
                max_run = run
        
        return max_run if max_prof > 0 else -1
