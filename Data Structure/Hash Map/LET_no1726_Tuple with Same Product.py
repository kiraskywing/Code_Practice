class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        res = 0
        record = collections.defaultdict(int)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                cur = nums[i] * nums[j]
                res += record[cur]
                record[cur] += 1
        return res * 8