class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for num in nums:
            k ^= num

        res = 0
        while k > 0:
            res += k & 1
            k >>= 1
        
        return res