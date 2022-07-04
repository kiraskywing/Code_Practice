class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, n, nums):

        if not nums or n > len(nums):
            return

        return self.helper(nums, 0, len(nums) - 1, n - 1)

    def helper(self, nums, left, right, k):

        if left == right:
            return nums[left]

        i, j = left, right
        pivot = nums[(i + j) // 2]

        while i <= j:

            while i <= j and nums[i] > pivot:
                i += 1
            while i <= j and nums[j] < pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        if k <= j:
            return self.helper(nums, left, j, k)
        if k >= i:
            return self.helper(nums, i, right, k)

        return nums[k]