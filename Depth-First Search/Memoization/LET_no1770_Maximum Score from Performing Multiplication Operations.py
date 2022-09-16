class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        return self.helper(nums, multipliers, 0, len(nums) - 1, 0, dict())
    
    def helper(self, nums1, nums2, left, right, i, memo):
        if i == len(nums2):
            return 0
        
        if (left, right, i) not in memo:
            memo[(left, right, i)] = max(
                nums1[left] * nums2[i] + self.helper(nums1, nums2, left + 1, right, i + 1, memo),
                nums1[right] * nums2[i] + self.helper(nums1, nums2, left, right - 1, i + 1, memo)
            )
        
        return memo[(left, right, i)]