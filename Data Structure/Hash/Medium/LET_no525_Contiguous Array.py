class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cur, res = 0, 0
        record = dict()
        for i in range(len(nums)):
            if nums[i] == 0:
                cur -= 1
            else:
                cur += 1
            
            if cur == 0:
                res = max(res, i + 1)
            else:
                if cur in record:
                    res = max(res, i - record[cur])
                else:
                    record[cur] = i
        return res