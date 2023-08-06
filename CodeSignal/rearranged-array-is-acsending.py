def solution(a):
    n = len(a)
    left, right = 0, n - 1
    prev, cur = left, right
    left += 1
    
    for i in range(1, n):
        if a[prev] >= a[cur]:
            return False
        
        prev = cur
        if i % 2 == 0:
            left += 1
            cur = right
        else:
            right -= 1
            cur = left
    
    return True
