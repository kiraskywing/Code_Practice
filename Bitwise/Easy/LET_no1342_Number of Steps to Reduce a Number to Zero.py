class Solution:
    def numberOfSteps (self, num: int) -> int:
        res = 0
        while num:
            if num & 1:
                num -= 1
                res += 1
                continue
            num >>= 1
            res += 1
        
        return res