def solution(s):
    n = len(s)
    left, right = 0, n - 1
    while left < right:
        
        while left < right and s[right] != s[left]:
            right -= 1
        
        if left < right and s[left:right+1] == s[left:right+1][::-1]:
            return solution(s[right+1:])
        
        right -= 1
    
    return s