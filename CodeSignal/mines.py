import collections

def solution(field, x, y):
    m, n = len(field), len(field[0])
    board = [[-1 for _ in range(n)] for _ in range(m)]
    
    queue = collections.deque([(x, y)])
    visited = {(x, y)}
    
    while queue:
        i, j = queue.popleft()
        counts = int(field[i][j] == True)
        temp = []
        
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                i2, j2 = i + di, j + dj
                if 0 <= i2 < m and 0 <= j2 < n:
                    counts += int(field[i2][j2] == True)
                    if board[i2][j2] == -1 and (i2, j2) not in visited:
                        temp.append((i2, j2))
        
        board[i][j] = counts
        if counts == 0:
            for i, j in temp:
                visited.add((i, j))
                queue.append((i, j))
    
    return board
