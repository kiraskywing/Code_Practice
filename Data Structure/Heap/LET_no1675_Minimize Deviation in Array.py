import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, (num // (num & -num), num))
        
        res = sys.maxsize
        maxVal = max(num2 for num2, num in pq)
        
        while len(pq) == len(nums):
            num2, num = heapq.heappop(pq)
            res = min(res, maxVal - num2)
            if num2 % 2 != 0 or num2 < num:
                num2 *= 2
                maxVal = max(maxVal, num2)
                heapq.heappush(pq, (num2, num))
        
        return res