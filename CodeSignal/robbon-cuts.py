def solution(a, k):
    min_size, max_size = 1, max(a)
    
    while min_size + 1 < max_size:
        mid_size = (min_size + max_size) // 2
        cuts = sum(size // mid_size for size in a)
        if cuts >= k:
            min_size = mid_size
        else:
            max_size = mid_size
            
    cuts = sum(size // max_size for size in a)
    if cuts >= k:
        return max_size
    return min_size
