def convert(arr, offset):
    res = []
    for row in arr:
        num = 0
        for d in row:
            num = num * 2 + d
        res.append(num << offset)
    return res

def solution(field, figure):
    cols_f = len(field[0])
    cols_p = len(figure[0])
    
    f, p = convert(field, 0), convert(figure, cols_f - cols_p)
    one_row = sum(1 << i for i in range(cols_f))
    m, n = len(f), len(p)
    
    for shift in range(cols_f - cols_p + 1):
        if shift > 0:
            for i in range(n):
                p[i] >>= 1
        
        for i in range(m - 1, n - 2, -1):
            has_one_row = False
            not_intersect = True
            for j in range(n):
                if (f[i - j] & p[n - 1 - j]) > 0:
                    not_intersect = False
                    break
                if (f[i - j] | p[n - 1 - j]) == one_row:
                    has_one_row = True
            
            if has_one_row and not_intersect:
                return shift
    
    return -1
