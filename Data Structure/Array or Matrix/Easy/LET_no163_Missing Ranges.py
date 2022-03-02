class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums.append(upper + 1)
        pre = lower - 1
        res = []
        for num in nums:
            if num == pre + 2:
                res.append(str(pre + 1))
            if num > pre + 2:
                res.append(str(pre + 1) + "->" + str(num - 1))
            pre = num
        return res