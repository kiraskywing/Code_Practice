class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        i, j, m, n = 0, 0, len(nums1), len(nums2)
        res = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
                while i < m and nums1[i] == res[-1]:
                    i += 1
                while j < n and nums2[j] == res[-1]:
                    j += 1
        return res