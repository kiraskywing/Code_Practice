import collections
from ctypes import resize

def black_count(i, j, memo):
    count = 0
    for (new_i, new_j) in [(i, j), (i+1, j), (i, j+1), (i+1, j+1)]:
        if new_i in memo and new_j in memo[new_i]:
            count += 1
    return count

def solution(rows, cols, black):
    memo = collections.defaultdict(set)
    for (i, j) in black:
        memo[i].add(j)

    res = [0 for _ in range(5)]
    visited = set()
    for i in memo:
        for j in memo[i]:
            for (di, dj) in [(-1, -1), (-1, 0), (0, -1), (0, 0)]:
                if 0 <= i+di < rows-1 and 0 <= j+dj < cols-1:
                    if (i+di, j+dj) not in visited:
                        count = black_count(i+di, j+dj, memo)
                        res[count] += 1
                        visited.add((i+di, j+dj))

    # (# all white) = (# total) - (# has black)
    res[0] = (rows-1) * (cols-1) - sum(res)

    return res

rows, cols = 3, 3
black = [[0, 0], [0, 1], [1, 0]]
print(solution(rows, cols, black)) # [1, 2, 0, 1, 0]