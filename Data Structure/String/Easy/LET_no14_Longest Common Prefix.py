class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = min(len(s) for s in strs)
        
        for j in range(size):
            for i in range(1, len(strs)):
                if strs[i - 1][j] != strs[i][j]:
                    return strs[0][:j]
        
        return strs[0][:size]