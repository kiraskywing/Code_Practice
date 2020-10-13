class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """

    def strStr2(self, source, target):
        if source is None or target is None:
            return -1

        m, n = len(target), len(source)
        if m == 0:
            return 0

        import random
        mod = random.randint(1000000, 2000000)
        hash_target = 0
        seed = 26

        for i in range(m):
            hash_target = (hash_target * seed + ord(target[i]) - ord('a')) % mod
            if hash_target < 0:
                hash_target += mod

        base = 1
        for i in range(m - 1):
            base = base * seed % mod

        hash_source = 0
        for i in range(n):
            if i >= m:
                hash_source = (hash_source - base * (ord(source[i - m]) - ord('a'))) % mod

            hash_source = (hash_source * seed + ord(source[i]) - ord('a')) % mod
            if hash_source < 0:
                hash_source += mod

            if i >= m - 1 and hash_target == hash_source:
                return i - m + 1

        return -1
