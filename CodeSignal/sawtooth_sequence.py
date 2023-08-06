def solution(arr):
    inc = dsc = 1  # length of increasing/decreasing
    n = len(arr)
    
    res = 0
    for i in range(1, n):
        inc_next = dsc_next = 1
        
        if arr[i] > arr[i-1]:
            inc_next = dsc + 1
            
        if arr[i] < arr[i-1]:
            dsc_next = inc + 1
        
        # compute how many subarray end at i
        inc, dsc = inc_next, dsc_next
        if inc >= 2:
            res += inc - 1
        if dsc >= 2:
            res += dsc - 1
            
    return res