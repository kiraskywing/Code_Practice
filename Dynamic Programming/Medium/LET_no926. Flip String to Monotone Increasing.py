class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = flips = 0
        for c in s:
            if c == '1':
                ones += 1
            else:
                flips += 1
            flips = min(flips, ones)
        return flips