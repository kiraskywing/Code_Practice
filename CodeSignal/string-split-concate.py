def solution(s):
    n = len(s)
    res = 0
    for i in range(1, n - 1):
        a = s[0:i]
        for j in range(i + 1, n):
            b = s[i:j]
            c = s[j:n]
            res += (a + b != b + c) and (b + c != c + a) and (a + b != c + a)

    return res