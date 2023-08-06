def slope_change(a, b):
    return a // abs(a) == b // abs(b)

def solution(arr):
    res = 0
    left, right = 0, 1
    n = len(arr)
    if n < 2:
        return 0
    
    while right < n:
        slope = arr[right] - arr[left]
        if slope == 0:
            left, right = left + 1, right + 1
            continue
            
        while right < n and arr[right] != arr[right - 1] and slope_change(arr[right] - arr[right - 1], slope):
            right += 1
            slope *= -1
            
        size = right - left
        res += size * (size - 1) // 2
    
    return res
