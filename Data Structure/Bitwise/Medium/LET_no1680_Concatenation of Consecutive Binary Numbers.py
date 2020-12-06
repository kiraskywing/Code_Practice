class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = cur_bits = 0
        mod = 10 ** 9 + 7
        
        # Method 1
        for x in range(1, n + 1):
            if x & -x == x:
                cur_bits += 1
            res = (res * (1 << cur_bits) + x) % mod
        
        # Method 2
        for x in range(1, n + 1):
            res = (res * (1 << (len(bin(x)) - 2)) + x) % mod
        
        return res