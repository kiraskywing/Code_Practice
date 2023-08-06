import collections

def solution(arr):
    queue = collections.deque([])
    for i in range(len(arr)):
        if arr[i]:
            queue.append((i, 0))
            
    res = []
    while queue:
        i, j = queue.popleft()
        res.append(arr[i][j])
        j += 1
        
        if j < len(arr[i]):
            queue.append((i, j))
    
    return ''.join(res)
