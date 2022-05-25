# Similar to LeetCode no300. Longest Increasing Subsequence

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        min_height = [float('inf')] * (n + 1)
        min_height[0] = float('-inf')
        
        for _, h in envelopes:
            idx = self.binarySearch(min_height, h)
            # idx = bisect.bisect_left(min_height, h)
            min_height[idx] = h
        
        for i in range(n, 0, -1):
            if min_height[i] != float('inf'):
                return i
        return -1
    
    def binarySearch(self, arr, target):
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid
            else:
                right = mid
        
        if arr[right] >= target:
            return right
        return left