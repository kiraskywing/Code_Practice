class Solution:
    def findLHS(self, nums: List[int]) -> int:
        record = collections.Counter(nums)
        res = 0
        for key in record:
            if key - 1 in record:
                res = max(res, record[key] + record[key - 1])
                
        return res