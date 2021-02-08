class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        sum1, sum2 = set(), set()
        self.getSum(0, 0, nums[:len(nums)//2], sum1)
        self.getSum(0, 0, nums[len(nums)//2:], sum2)
        
        sum2 = sorted(sum2)
        res = abs(goal)
        
        for num in sum1:
            remain = goal - num
            i = bisect.bisect_left(sum2, remain)
            if i < len(sum2):
                res = min(res, abs(remain - sum2[i]))
            if i > 0:
                res = min(res, abs(remain - sum2[i - 1]))
        
        return res
        
    def getSum(self, i, cur_sum, arr, record):
        if i == len(arr):
            record.add(cur_sum)
            return
        self.getSum(i + 1, cur_sum, arr, record)
        self.getSum(i + 1, cur_sum + arr[i], arr, record)