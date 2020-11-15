class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        bCount = res = 0
        for i in range(n):
            if s[i] == 'b':
                bCount += 1
            elif s[i] == 'a' and bCount > 0:
                res += 1
                bCount -= 1
        return res