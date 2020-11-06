class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0

        minlast = [sys.maxsize] * (len(nums) + 1)
        minlast[0] = -sys.maxsize

        for i in range(len(nums)):
            index = self.binarysearch(minlast, nums[i])
            minlast[index] = nums[i]

        for i in range(len(nums), 0, -1):
            if minlast[i] != sys.maxsize:
                return i

        return 0

    def binarysearch(self, arr, target):
        left, right = 0, len(arr) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid
            else:
                right = mid

        return right
