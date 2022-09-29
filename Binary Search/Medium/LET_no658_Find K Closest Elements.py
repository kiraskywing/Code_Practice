class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        upper_idx = self.get_first_upper(arr, x)
        lower_idx = upper_idx - 1
        n = len(arr)
        
        for _ in range(k):
            if self.choose_lower(arr, lower_idx, upper_idx, x):
                lower_idx -= 1
            else:
                upper_idx += 1
        
        return arr[lower_idx + 1:upper_idx]
        
    def get_first_upper(self, arr, target):
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                right = mid
            else:
                left = mid
                
        if arr[left] >= target:
            return left
        if arr[right] >= target:
            return right
        return len(arr)
    
    def choose_lower(self, arr, lower, upper, target):
        if upper >= len(arr):
            return True
        if lower < 0:
            return False
        return target - arr[lower] <= arr[upper] - target