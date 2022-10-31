class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1

        min_day, max_day = 1, max(bloomDay) 
        while min_day + 1 < max_day:    # O(log(max(bloomDay)))
            mid_day = (min_day + max_day) // 2
            bouquets = self.helper(bloomDay, mid_day, k)    # O(n)
            if bouquets >= m:
                max_day = mid_day
            else:
                min_day = mid_day

        # => total time: O(n * log(max(bloomDay)))

        if self.helper(bloomDay, min_day, k) >= m:
            return min_day
        if self.helper(bloomDay, max_day, k) >= m:
            return max_day
        return -1
    
    def helper(self, arr, limit, k):
        count = 0
        adjacents = 0
        for day in arr:
            if day <= limit:
                adjacents += 1
            else:
                adjacents = 0

            if adjacents == k:
                count += 1
                adjacents = 0

        return count