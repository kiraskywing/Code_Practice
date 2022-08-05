class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        size = min(steps // 2 + 1, arrLen)
        cur, prev = [0] * (size + 2), [0] * (size + 2)
        prev[1] = 1
        
        for _ in range(steps):
            for i in range(1, size + 1):
                cur[i] = (prev[i - 1] + prev[i] + prev[i + 1]) % (10 ** 9 + 7)
            prev, cur = cur, prev
        
        return prev[1]