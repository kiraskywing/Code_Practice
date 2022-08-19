class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if (m + n) % 2 != 0:
            return self.findKth(nums1, nums2, (m + n) // 2 + 1) * 1.0
        else:
            first = self.findKth(nums1, nums2, (m + n) // 2)
            second = self.findKth(nums1, nums2, (m + n) // 2 + 1)
            return (first + second) / 2
        
    def findKth(self, nums1, nums2, k):
        min_val = max_val = 0
        if nums1:
            min_val, max_val = min(min_val, min(nums1)), max(max_val, max(nums1))
        if nums2:
            min_val, max_val = min(min_val, min(nums2)), max(max_val, max(nums2))
            
        while min_val + 1 < max_val:
            mid_val = (min_val + max_val) // 2
            count = self.countHelper(nums1, nums2, mid_val)
            if count >= k:
                max_val = mid_val
            else:
                min_val = mid_val
                
        count = self.countHelper(nums1, nums2, max_val)
        if count >= k:
            return max_val
        
        return min_val
        
    def countHelper(self, nums1, nums2, target):
        return self.countLessEqualTarget(nums1, target) + self.countLessEqualTarget(nums2, target)
        # return bisect.bisect_right(nums1, target) + bisect.bisect_right(nums2, target)
    
    def countLessEqualTarget(self, nums, target):
        if not nums:
            return 0
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
                
        if nums[right] <= target:
            return right + 1
        if nums[left] <= target:
            return left + 1
        return 0