# The same as LeetCode no28 Implement strStr()

class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        if not target:
            return 0
        
        n, m = len(source), len(target)
        for i in range(n - m + 1):
            j = 0
            while j < m and source[i + j] == target[j]:
                j += 1
            if j == m:
                return i

        return -1