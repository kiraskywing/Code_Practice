class Solution:
    def firstUniqChar(self, s: str) -> int:
        memo = collections.Counter(s)
        for i in range(len(s)):
            if memo[s[i]] == 1:
                return i
        return -1