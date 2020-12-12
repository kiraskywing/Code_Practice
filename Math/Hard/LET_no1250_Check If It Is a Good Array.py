class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:

        gcd = nums[0]

        for elem in nums:
            while elem:
                gcd, elem = elem, gcd % elem

        return gcd == 1