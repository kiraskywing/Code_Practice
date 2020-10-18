class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxLen, rec = -1, {}
        for i, ch in enumerate(s):
            maxLen = max(maxLen, i - rec.setdefault(ch, i) - 1)
        return maxLen
        
        # res, rec = -1, {}
        # for i in range(len(s)):
        #     if s[i] not in rec: rec[s[i]] = i
        #     else: res = max(res, i - rec[s[i]] - 1)
        # return res