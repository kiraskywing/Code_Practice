class Solution:
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
