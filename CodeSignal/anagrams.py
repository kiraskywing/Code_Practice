import collections

def solution(a):
    memo = collections.defaultdict(int)
    for num in a:
        s = ''.join(sorted(str(num)))
        memo[s] += 1
        
    res = 0
    for val in memo.values():
        if val >= 2:
            res += val * (val - 1) // 2
    
    return res
