from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """
    def copy_books_i_i(self, n: int, times: List[int]) -> int:
        left, right = 0, n * min(times)
        while left + 1 < right:
            mid = (left + right) // 2
            if self.count(times, mid) < n:
                left = mid
            else:
                right = mid
        
        if self.count(times, left) >= n:
            return left
        return right

    def count(self, times, total_time):
        return sum(total_time // time for time in times)
