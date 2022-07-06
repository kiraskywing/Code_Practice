class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if (m + n) % 2 != 0:
            return self.helper(nums1, nums2, (m + n) // 2) * 1.0
        else:
            first = self.helper(nums1, nums2, (m + n) // 2 - 1)
            second = self.helper(nums1, nums2, (m + n) // 2)
            return (first + second) / 2
        
    def helper(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        
        mid1, mid2 = len(nums1) // 2, len(nums2) // 2
        val1, val2 = nums1[mid1], nums2[mid2]
        if mid1 + mid2 < k:
            if val1 > val2:
                return self.helper(nums1, nums2[mid2 + 1:], k - (mid2 + 1))
            else:
                return self.helper(nums1[mid1 + 1:], nums2, k - (mid1 + 1))
        else:
            if val1 > val2:
                return self.helper(nums1[:mid1], nums2, k)
            else:
                return self.helper(nums1, nums2[:mid2], k)