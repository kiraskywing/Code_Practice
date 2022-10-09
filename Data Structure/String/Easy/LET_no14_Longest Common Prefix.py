class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = min(len(s) for s in strs)
        
        for j in range(size):
            for i in range(1, len(strs)):
                if strs[i - 1][j] != strs[i][j]:
                    return strs[0][:j]
        
        return strs[0][:size]

class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while True:
            prev = None
            for s in strs:
                if i == len(s):
                    return s[:i]
                if prev and s[i] != prev:
                    return s[:i]
                prev = s[i]
            i += 1
        
        return ""