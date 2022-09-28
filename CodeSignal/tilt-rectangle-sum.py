def solution(matrix, a, b):
    # topest i, j -> (i2, j2) = i + (a - 1), j - (a - 1)
    #             -> (i3, j3) = i + (b - 1), j + (b - 1)
    #             -> (i4, j4) = i2 + (b - 1), j2 + (b - 1)
    
    # topest i, j -> (i2, j2) = i + (b - 1), j - (b - 1)
    #             -> (i3, j3) = i + (a - 1), j + (a - 1)
    #             -> (i4, j4) = i2 + (a - 1), j2 + (a - 1)
    
    #     i
    #
    #  i2        i3
    #
    #         i4

    # 0, 0, 1, 0, 0, 0
    # 0, 1, 1, 1, 0, 0
    # 0, 0, 1, 1, 1, 0
    # 0, 0, 0, 1, 0, 0
    # 0, 0, 0, 0, 0, 0

    # 0, 0, 1, 0, 0, 0
    # 0, 1, 1, 1, 0, 0
    # 1, 1, 1, 0, 0, 0
    # 0, 1, 0, 0, 0, 0
    # 0, 0, 0, 0, 0, 0
    
    m, n = len(matrix), len(matrix[0])
    for i in range(1, m):
        for j in range(1, n):
            matrix[i][j] += matrix[i - 1][j - 1]
            
    res = float('-inf')
    for i in range(m):
        for j in range(n):
            i3, j3 = helper(m, n, i, j, a, b)
            if -1 not in (i3, j3):
                cur = get_sum(matrix, i, j, i3, j3, a * 2 - 1)
                print(i, j, i3, j3, cur)
                res = max(res, cur)
                
            i3, j3 = helper(m, n, i, j, b, a)
            if -1 not in (i3, j3):
                cur = get_sum(matrix, i, j, i3, j3, b * 2 - 1)
                print(i, j, cur)
                res = max(res, cur)
                
    return res

def helper(m, n, i, j, a, b):
    i2, j2 = i + (a - 1), j - (a - 1)
    if not (0 <= i2 < m and 0 <= j2 < n):
        return -1, -1
        
    i3, j3 = i + (b - 1), j + (b - 1)
    if not (0 <= i3 < m and 0 <= j3 < n):
        return -1, -1
        
    i4, j4 = i2 + (b - 1), j2 + (b - 1)
    if not (0 <= i4 < m and 0 <= j4 < n):
        return -1, -1
    
    return i3, j3
    
def get_sum(matrix, i, j, i3, j3, times):
    cur = 0
    for k in range(times):
        cur += matrix[i3][j3] - (matrix[i - 1][j - 1] if i > 0 and j > 0 else 0)
        if k % 2 == 0:
            i += 1
            j3 -= 1
        else:
            j -= 1
            i3 += 1
    
    return cur