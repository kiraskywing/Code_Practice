class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for n in nums: 
            diff ^= n
        diff &= -diff
        res = [0, 0]
        for n in nums:
            if diff & n:
                res[0] ^= n
            else:
                res[1] ^= n
        return res