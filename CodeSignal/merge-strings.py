import collections

def solution(s1, s2):
    memo1 = collections.Counter(s1)
    memo2 = collections.Counter(s2)
    
    res = []
    m, n = len(s1), len(s2)
    i = j = 0
    while i < m and j < n:
        c1, c2 = s1[i], s2[j]
        if memo1[c1] < memo2[c2] or (memo1[c1] == memo2[c2] and c1 <= c2):
            res.append(c1)
            i += 1
        else:
            res.append(c2)
            j += 1
            
    if i < m:
        res.append(s1[i:])
    if j < n:
        res.append(s2[j:])
    
    return ''.join(res)
