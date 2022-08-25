class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        
        res = up = down = 0
        for i in range(1, n):
            if down > 0 and arr[i - 1] <= arr[i]:
                up = down = 0
            
            up += arr[i - 1] < arr[i]
            down += arr[i - 1] > arr[i]
            if up > 0 and down > 0:
                res = max(res, up + down + 1)
        
        return res

class Solution2:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        
        incr_from_left = [1] * n
        incr_from_right = 1
        
        res = 0
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                incr_from_left[i] += incr_from_left[i - 1]
        
        for j in range(n - 2, -1, -1):
            if arr[j] > arr[j + 1]:
                incr_from_right += 1
                if incr_from_left[j] > 1:
                    res = max(res, incr_from_left[j] + incr_from_right - 1)
            else:
                incr_from_right = 1
        
        return res