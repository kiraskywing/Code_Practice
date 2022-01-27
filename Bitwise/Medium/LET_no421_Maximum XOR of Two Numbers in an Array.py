class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= 1 << i
            prefix = set([num & mask for num in nums])
            start = res | 1 << i
            for pre in prefix:
                if start ^ pre in prefix:
                    res = start
                    break
        return res