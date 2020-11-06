class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        for i in reversed(range(32)):
            prefixes = set([x >> i for x in nums])
            ans <<= 1
            cur = ans + 1
            for p in prefixes:
                if cur ^ p in prefixes:
                    ans = cur
                    break
        return ans