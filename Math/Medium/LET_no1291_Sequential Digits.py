class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        queue = collections.deque(range(1, 10))
        while queue:
            cur = queue.popleft()
            if low <= cur <= high:
                res.append(cur)
            last = cur % 10
            if last + 1 < 10:
                queue.append(cur * 10 + last + 1)
        return res