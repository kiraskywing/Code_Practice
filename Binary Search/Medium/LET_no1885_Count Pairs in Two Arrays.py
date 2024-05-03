class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        nums = [x - y for x, y in zip(nums1, nums2)]
        nums.sort()
        n = len(nums)
        res = 0

        for i, diff in enumerate(nums):
            idx = self.idx_no_less_than_target(nums, -diff + 1)
            res += n - max(i + 1, idx)

        return res

    def idx_no_less_than_target(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        
        if nums[left] >= target:
            return left
        if nums[right] >= target:
            return right
        return len(nums)