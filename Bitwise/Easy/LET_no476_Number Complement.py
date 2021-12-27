class Solution:
    def findComplement(self, num: int) -> int:
        res = 1
        while res <= num:
            res <<= 1
        
        return num ^ res - 1