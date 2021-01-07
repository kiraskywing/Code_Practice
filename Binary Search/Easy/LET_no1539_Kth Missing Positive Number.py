class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] - (mid + 1) < k:
                left = mid
            else:
                right = mid
        
        if arr[left] - (left + 1) >= k:
            return left + k
        elif arr[right] - (right + 1) >= k:
            return right + k
        return len(arr) + k