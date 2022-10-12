class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        for i in range(n - 2):
            left, right = i + 1, i + 2
            if nums[left] + nums[right] > nums[i]:
                return nums[i] + nums[left] + nums[right]
        
        return 0