class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        pres = [0] * n
        memo = collections.defaultdict(list)
        for a, b in relations:
            pres[b - 1] += 1
            memo[a - 1].append(b - 1)
            
        queue = collections.deque([i for i in range(n) if pres[i] == 0])
        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                for nxt in memo[cur]:
                    pres[nxt] -= 1
                    if pres[nxt] == 0:
                        queue.append(nxt)
        
        return -1 if any(num for num in pres) else count