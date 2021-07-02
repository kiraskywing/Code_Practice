class Solution:
    def hammingWeight(self, n: int) -> int:
        # Solution 1
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res
        
        # Solution 2
        return sum(int(x) for x in bin(n)[2:])