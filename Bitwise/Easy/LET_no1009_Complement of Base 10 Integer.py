class Solution:
    def bitwiseComplement(self, N: int) -> int:
        x = 1
        while x < N:
            x = x * 2 + 1
        return x - N