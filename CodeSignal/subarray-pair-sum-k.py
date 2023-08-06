import collections

def solution(a, m, k):
    memo = collections.defaultdict(int)
    pairs = set()
    
    for num1 in a[:m]:
        num2 = k - num1
        if memo[num2] > 0:
            pairs.add((min(num1, num2), max(num1, num2)))
        memo[num1] += 1
    
    res = int(len(pairs) > 0)
        
    left = 0
    for right in range(m, len(a)):
        num1 = a[left]
        num2 = k - num1
        
        if memo[num1] > 1:
            memo[num1] -= 1
            if num1 == num2 and memo[num1] == 1:
                pairs.remove((min(num1, num2), max(num1, num2)))
        else:
            memo[num1] -= 1
            if memo[num2] > 0:
                pairs.remove((min(num1, num2), max(num1, num2)))
        
        left += 1
        
        num1 = a[right]
        num2 = k - num1
        if memo[num2] > 0:
            pairs.add((min(num1, num2), max(num1, num2)))
        
        res += len(pairs) > 0
        memo[num1] += 1
    
    return res

a = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7]
m = 4
k = 10
print(solution(a, m, k))

a = [15, 8, 8, 2, 6, 4, 1, 7]
m = 2
k = 8
print(solution(a, m, k))

a, m, k = [5, 2, 10, 8, 9, 8, 2, 6, 2], 4, 10
print(solution(a, m, k)) # 5

a, m, k = [2, 1, 1, 2, 3, 1, 1, 2, 1, 2, 1, 3, 1, 2, 1, 3], 3, 4
print(solution(a, m, k)) # 8