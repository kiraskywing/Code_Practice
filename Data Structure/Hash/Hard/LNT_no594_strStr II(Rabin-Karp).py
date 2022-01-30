class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    def strStr2(self, source, target):
        if source is None or target is None:
            return -1
        if not target:
            return 0

        base = 33
        mod = 1000000007
        key = 1
        sHash = [key]
        for c in source:
            key = (key * base + ord(c) - ord('a')) % mod
            sHash.append(key)

        key = 1
        for c in target:
            key = (key * base + ord(c) - ord('a')) % mod
        tHash = key

        
        key, n = 1, len(target)
        for _ in range(n):
            key = key * base % mod
        order = key

        tHash = (tHash - order + mod) % mod

        for i in range(len(source) - n + 1):
            val = (sHash[i + n] - sHash[i] * order % mod + mod) % mod
            if val == tHash:
                return i
        
        return -1
