from typing import (
    List,
)

class Solution:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """
    def string_replace(self, a: List[str], b: List[str], s: str) -> str:
        base = 33
        mod = 10 ** 9 + 7
        max_length = -1
        a_hash, s_hash, order = [], [], []

        for string in a:
            key = 1
            max_length = max(max_length, len(string))
            for c in string:
                key = (key * base + ord(c) - ord('a')) % mod
            a_hash.append(key)
        
        key = 1
        s_hash.append(key)
        max_length = max(max_length, len(s))
        for c in s:
            key = (key * base + ord(c) - ord('a')) % mod
            s_hash.append(key)
        
        key = 1
        order.append(key)
        for _ in range(max_length):
            key = key * base % mod
            order.append(key)
        
        res = list(s)
        i = 0
        while i < len(s):
            max_length = target = 0
            for j in range(len(a)):
                a_size = len(a[j])
                if i + a_size > len(res):
                    continue
                
                s_val = (s_hash[i + a_size] - s_hash[i] * order[a_size] % mod + mod) % mod
                a_val = (a_hash[j] - order[a_size] + mod) % mod

                if s_val == a_val and a_size > max_length:
                    max_length = a_size
                    target = j
            
            if max_length > 0:
                for j in range(max_length):
                    res[i + j] = b[target][j]
                i += max_length
            else:
                i += 1
        
        return ''.join(res)
