class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        m, n = len(v1), len(v2)
        i = j = 0
        
        while i < m and j < n:
            if int(v1[i]) < int(v2[j]):
                return -1
            elif int(v1[i]) > int(v2[j]):
                return 1
            i += 1
            j += 1

        while i < m:
            if int(v1[i]) > 0:
                return 1
            i += 1
        while j < n:
            if int(v2[j]) > 0:
                return -1
            j += 1
        
        return 0