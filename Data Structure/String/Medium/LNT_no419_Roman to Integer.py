# The same as LeetCode no13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        memo = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        pre = res = 0
        for c in reversed(s):
            cur = memo[c]
            if cur < pre:
                res -= cur
                pre = 0
            else:
                res += cur
                pre = cur
        return res