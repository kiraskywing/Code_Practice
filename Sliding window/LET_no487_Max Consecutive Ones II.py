class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev = -1
        cur = res = 0
        for num in nums:
            if num == 0:
                prev, cur = cur, 0
            else:
                cur += 1
            
            res = max(res, prev + cur + 1)
        
        return res