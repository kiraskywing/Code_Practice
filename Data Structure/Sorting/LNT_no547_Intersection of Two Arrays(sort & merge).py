class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """

    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        i, j, result = 0, 0, []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if not result or result[-1] != nums1[i] and result[-1] != nums2[j]:
                    result.append(nums1[i])
                i += 1;
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result