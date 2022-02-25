class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        if n % 2 != 0:
            return self.get_kth(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, n // 2) * 1.0
        else:
            first = self.get_kth(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, n // 2)
            second = self.get_kth(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, n // 2 - 1)
            return (first + second) / 2
        
    def get_kth(self, A, s1, e1, B, s2, e2, k):
        if s1 > e1:
            return B[k - s1]
        if s2 > e2:
            return A[k - s2]
        
        mid_a = (s1 + e1) // 2
        mid_b = (s2 + e2) // 2
        val_a, val_b = A[mid_a], B[mid_b]
        
        if mid_a + mid_b < k:
            if val_a > val_b:
                return self.get_kth(A, s1, e1, B, mid_b + 1, e2, k)
            else:
                return self.get_kth(A, mid_a + 1, e1, B, s2, e2, k)
        else:
            if val_a > val_b:
                return self.get_kth(A, s1, mid_a - 1, B, s2, e2, k)
            else:
                return self.get_kth(A, s1, e1, B, s2, mid_b - 1, k)