class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):
        len_a, len_b = len(A), len(B)
        if (len_a + len_b) % 2 == 1:
            return self.find_kth(A, B, (len_a + len_b) // 2 + 1)
        else:
            smaller = self.find_kth(A, B, (len_a + len_b) // 2)
            larger = self.find_kth(A, B, (len_a + len_b) // 2 + 1)
            return (smaller + larger) / 2

    def find_kth(self, A, B, k):
        if not A:
            min_val, max_val = B[0], B[-1]
        elif not B:
            min_val, max_val = A[0], A[-1]
        else:
            min_val, max_val = min(A[0], B[0]), max(A[-1], B[-1])

        while min_val + 1 < max_val:
            mid = (min_val + max_val) // 2
            count1 = self.counter(A, mid)
            count2 = self.counter(B, mid)
            if count1 + count2 < k:
                min_val = mid
            else:
                max_val = mid

        count1 = self.counter(A, min_val)
        count2 = self.counter(B, min_val)
        if count1 + count2 >= k:
            return min_val
        else:
            return max_val

    def counter(self, array, target):
        if not array:
            return 0

        i, j = 0, len(array) - 1
        while i + 1 < j:
            mid = (i + j) // 2
            if array[mid] <= target:
                i = mid
            else:
                j = mid

        if array[j] <= target:
            return j + 1
        if array[i] <= target:
            return i + 1
        return 0

    # def counter(self, nums1, nums2, target):
    #     return bisect.bisect(nums1, target) + bisect.bisect(nums2, target)