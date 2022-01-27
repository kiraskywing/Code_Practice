class Solution:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """
    def stringReplace(self, a, b, s):
        base = 33
        mod = 1000000007
        maxLen = -1
        aHash, sHash, order = [], [], []

        for sub in a:
            key = 1
            maxLen = max(maxLen, len(sub))
            for c in sub:
                key = (key * base + ord(c) - ord('a')) % mod
            aHash.append(key)
        
        key = 1
        sHash.append(key)
        maxLen = max(maxLen, len(s))
        for c in s:
            key = (key * base + ord(c) - ord('a')) % mod
            sHash.append(key)

        key = 1
        order.append(key)
        for _ in range(maxLen):
            key = key * base % mod
            order.append(key)
        
        res = list(s)
        i = 0
        while i < len(res):
            maxLen, target = 0, 0
            for j in range(len(a)):
                aSize = len(a[j])
                if i + aSize > len(res):
                    continue
                
                sVal = (sHash[i + aSize] - sHash[i] * order[aSize] % mod + mod) % mod
                aVal = (aHash[j] - order[aSize] + mod) % mod
                
                if sVal == aVal and aSize > maxLen:
                    maxLen = aSize
                    target = j
            
            if maxLen > 0:
                for j in range(maxLen):
                    res[i + j] = b[target][j]
                i += maxLen
            else:
                i += 1
        
        return ''.join(res)
