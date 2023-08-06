def solution(pattern, source):
    vowels = {'a','e','i','o','u','y'}
    s = ''.join('0' if c in vowels else '1' for c in source)
    
    res = 0
    for i in range(len(s) - len(pattern) + 1):
        res += s[i:i+len(pattern)] == pattern
    
    return res
