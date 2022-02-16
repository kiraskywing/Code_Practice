# The same as LeetCode no.268. Missing Number
class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        i = 0
        for num in nums:
            res ^= num
            res ^= i
            i += 1
        return res

class Solution2:
    """
    @param nums: An array of integers
    @return: An integer
    """

    def findMissing(self, nums):
        n = len(nums)
        i = 0

        while i < n:
            while i != nums[i] and nums[i] < n:
                temp = nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]
            i += 1

        for i in range(n):
            if nums[i] != i:
                return i
        return n
