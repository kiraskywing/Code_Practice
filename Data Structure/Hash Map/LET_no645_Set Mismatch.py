class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        temp = collections.Counter(nums)
        for i in range(1, len(nums) + 1):
            if temp[i] == 2:
                twice = i
            if temp[i] == 0:
                once = i
        return twice, once
                