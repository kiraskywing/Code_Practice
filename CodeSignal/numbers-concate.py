def solution(a):
    offsets = sum(10 ** len(str(num)) for num in a)
    
    res = 0
    n = len(a)
    for num in a:
        res += num * n + num * offsets
    
    return res
