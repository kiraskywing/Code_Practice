class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones = arr.count(1)
        if ones == 0:
            return [0, len(arr) - 1]
        if ones % 3 != 0:
            return [-1, -1]
        
        k = ones // 3
        count = start = mid = end = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                count += 1
                if count == 1:
                    start = i
                elif count == k + 1:
                    mid = i
                elif count == 2 * k + 1:
                    end = i
                    break
        
        while end < len(arr) and arr[start] == arr[mid] == arr[end]:
            start += 1
            mid += 1
            end += 1
        
        if end == len(arr):
            return [start - 1, mid]
        return [-1, -1]