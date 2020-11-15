class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        upper = max([x] + forbidden) + a + b
        pos = [0] + [sys.maxsize] * upper
        for i in forbidden:
            pos[i] = -1
        
        queue = collections.deque([0])
        while queue:
            cur = queue.popleft()
            
            if cur + a <= upper and pos[cur + a] > pos[cur] + 1:
                pos[cur + a] = pos[cur] + 1
                queue.append(cur + a)
            if cur - b > 0 and pos[cur - b] > pos[cur] + 1:
                pos[cur - b] = pos[cur] + 1
                if cur - b + a <= upper and pos[cur - b + a] > pos[cur] + 2:
                    pos[cur - b + a] = pos[cur] + 2
                    queue.append(cur - b + a)
        
        return pos[x] if pos[x] < sys.maxsize else -1