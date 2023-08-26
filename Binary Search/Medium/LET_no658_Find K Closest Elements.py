class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lower = self.get_first_lower(arr, x)
        upper = lower + 1
        for _ in range(k):
            if self.is_lower(arr, lower, upper, x):
                lower -= 1
            else:
                upper += 1
        
        return arr[lower + 1 : upper]

    def get_first_lower(self, arr, target):
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                right = mid
            else:
                left = mid
        
        return right if arr[right] <= target else left

    def is_lower(self, arr, i, j, target):
        m = len(arr)
        if j == m:
            return True
        if i < 0:
            return False
        
        return target - arr[i] <= arr[j] - target