class Solution:
    def minJumps(self, arr: List[int]) -> int:
        indices = collections.defaultdict(list)
        n = len(arr)
        for i in range(n):
            indices[arr[i]].append(i)
        
        visited_pos = [False] * n
        visited_pos[0] = True
        visited_num = set()
        
        q = collections.deque([(0, 0)])
        
        while q:
            pos, steps = q.popleft()
            if pos == n - 1:
                return steps
            
            for nxt in [pos - 1, pos + 1] + indices[arr[pos]] * (arr[pos] not in visited_num):
                if 0 <= nxt <= n - 1 and not visited_pos[nxt]:
                    visited_pos[nxt] = True
                    q.append((nxt, steps + 1))
            
            visited_num.add(arr[pos])