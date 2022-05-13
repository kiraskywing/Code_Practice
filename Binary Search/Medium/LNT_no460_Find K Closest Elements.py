# The same as LeetCode no658. Find K Closest Elements

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # right = bisect.bisect_right(arr, x)
        right = self.find_upper(arr, x)
        left = right - 1
        res = []
        
        for _ in range(k):
            if self.choose_left(arr, left, right, x):
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
        
        return res
    
    def find_upper(self, arr, target):
        left, right = 0, len(arr) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                right = mid
            else:
                left = mid
        
        if arr[left] >= target:
            return left
        return right
    
    def choose_left(self, arr, left, right, target):
        if left < 0:
            return False
        if right >= len(arr):
            return True
        return target - arr[left] <= arr[right] - target