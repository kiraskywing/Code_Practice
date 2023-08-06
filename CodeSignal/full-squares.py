def get_max_pair_sum(arr):
    max_val = second_max_val = float('-inf')
    for num in arr:
        if num > max_val:
            second_max_val = max_val
            max_val = num
        elif num > second_max_val:
            second_max_val = num
    
    return max_val + second_max_val
    
def get_squares(num):
    res = [0]
    cur = i = 1
    while cur <= num:
        res.append(cur)
        i += 1
        cur = i ** 2
    
    return res
    
def count_pairs(cur, squares, numbers):
    res = 0
    for square in squares:
        target = square - cur
        res += target in numbers and target > cur
    
    return res

def solution(numbers):
    n = len(numbers)
    if n < 2:
        cur = numbers[0]
        if cur >= 0 and (cur * 2) ** 0.5 == int((cur * 2) ** 0.5):
            return 1
        return 0
    
    max_pair_sum = get_max_pair_sum(numbers)
    squares = get_squares(max_pair_sum)
    
    numbers = set(numbers)
    count = 0
    for cur in numbers:
        count += count_pairs(cur, squares, numbers)
        count += cur >= 0 and (cur * 2) ** 0.5 == int((cur * 2) ** 0.5)
    
    return count
