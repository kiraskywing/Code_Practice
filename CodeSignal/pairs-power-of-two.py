import collections

def solution(numbers):
    upper_bound = max(numbers) * 2
    candidates = set()
    cur = 1
    while cur <= upper_bound:
        candidates.add(cur)
        cur <<= 1
        
    memo = collections.defaultdict(int)
    res = 0
    for num in numbers:
        memo[num] += 1
        for target in candidates:
            res += memo[target - num]
    
    return res
