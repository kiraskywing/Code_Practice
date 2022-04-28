from typing import (
    List,
)

class Solution:
    """
    @param boxes: number of pens for each box
    @param target: the target number
    @return: the minimum boxes
    """
    def minimum_boxes(self, boxes: List[int], target: int) -> int:
        n = len(boxes)
        memo = [n for _ in range(n)]
        left, right, cur = n - 1, n - 1, 0
        while left >= 0:
            cur += boxes[left]
            while cur > target:
                cur -= boxes[right]
                right -= 1
            while right > left and boxes[right] == 0:
                right -= 1
            if cur == target:
                memo[left] = right - left + 1
            if left + 1 < n:
                memo[left] = min(memo[left], memo[left + 1])
            left -= 1

        left, right, cur = 0, 0, 0
        res = n + 1
        while right < n:
            cur += boxes[right]
            while cur > target:
                cur -= boxes[left]
                left += 1
            while left < right and boxes[left] == 0:
                left += 1
            if cur == target and right + 1 < n:
                res = min(res, right - left + 1 + memo[right + 1])
            right += 1
        
        return res if res < n + 1 else -1
