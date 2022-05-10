class Solution:
    """
    @param source: A source string
    @param target: A target string
    @return: An integer as index
    """
    def str_str2(self, source: str, target: str) -> int:
        if source is None or target is None or len(target) > len(source):
            return -1
        if not target:
            return 0
        
        base = 33
        mod = 10 ** 9 + 7
        key = 1
        s_hash = [key]
        for c in source:
            key = (key * base + ord(c) - ord('a')) % mod
            s_hash.append(key)

        t_hash = 1
        order = 1
        for c in target:
            t_hash = (t_hash * base + ord(c) - ord('a')) % mod
            order = order * base % mod
        t_hash = (t_hash - order + mod) % mod

        for i in range(len(source) - len(target) + 1):
            val = (s_hash[i + len(target)] - s_hash[i] * order + mod) % mod
            if val == t_hash:
                return i
        
        return -1
