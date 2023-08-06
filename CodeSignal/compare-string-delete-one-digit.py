def solution(s, t):
    m, n = len(s), len(t)
    s_digits = [i for i in range(m) if s[i].isdigit()]
    t_digits = [i for i in range(n) if t[i].isdigit()]
    
    res = 0
    for i in s_digits:
        s2 = s[:i] + s[i+1:]
        res += s2 < t
    
    for j in t_digits:
        t2 = t[:j] + t[j+1:]
        res += s < t2
    
    return res
