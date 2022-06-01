# The same as Leetcode no88. Merge Sorted Array

class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """

    def mergeSortedArray(self, A, m, B, n):

        while n > 0:

            if m == 0 or B[n - 1] > A[m - 1]:
                A[m + n - 1] = B[n - 1]
                n -= 1
            else:
                A[m + n - 1] = A[m - 1]
                m -= 1

class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total = m + n
        i, j = m - 1, n - 1
        for idx in range(total - 1, -1, -1):
            if j < 0 or i >= 0 and nums1[i] > nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
            elif i < 0 or j >= 0 and nums1[i] <= nums2[j]:
                nums1[idx] = nums2[j]
                j -= 1