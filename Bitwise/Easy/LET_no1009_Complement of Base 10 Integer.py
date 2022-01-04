class Solution:
    def bitwiseComplement(self, n: int) -> int:
        res = 1
        while res < n:
            res = (res << 1) + 1
            
        return res ^ n