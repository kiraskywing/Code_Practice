import heapq


class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        if not arrays:
            return []

        heap = []
        for index, array in enumerate(arrays):
            if array:
                heapq.heappush(heap, (array[0], index, 0))

        result = []
        while heap:
            value, index, sub_index = heapq.heappop(heap)
            result.append(value)
            if sub_index + 1 < len(arrays[index]):
                heapq.heappush(heap, (arrays[index][sub_index + 1], index, sub_index + 1))

        return result
