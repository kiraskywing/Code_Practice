class Solution:
    def appealSum(self, s: str) -> int:
        memo = {}
        cur = res = 0
        for i, c in enumerate(s):
            if c not in memo:
                cur += i + 1
            else:
                cur += i - memo[c]
            res += cur
            memo[c] = i
        return res