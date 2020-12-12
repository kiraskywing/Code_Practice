import heapq

class Solution:
    """
    @param nums: an integer unsorted array
    @param k: an integer from 1 to n
    @return: the kth largest element
    """
    def kthLargestElement2(self, nums, k):
        heap = []
        for val in nums:
            heapq.heappush(heap, val)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)
