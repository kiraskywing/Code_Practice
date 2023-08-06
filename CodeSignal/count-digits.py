import collections

def solution(a):
    s = ''.join(str(num) for num in a)
    memo = collections.Counter(s)
    
    count = max(memo.values())
    
    res = [int(c) for c in memo if memo[c] == count]
    res.sort()
    return res
