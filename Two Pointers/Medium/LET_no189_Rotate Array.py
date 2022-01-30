class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.rev_helper(nums, 0, len(nums) - 1)
        self.rev_helper(nums, 0, k - 1)
        self.rev_helper(nums, k, len(nums) - 1)
    
    def rev_helper(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1