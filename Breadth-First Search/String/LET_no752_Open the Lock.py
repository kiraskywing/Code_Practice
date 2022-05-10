class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:    # corner case
            return -1
        steps = 0
        queue = collections.deque(["0000"])
        
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == target:
                    return steps
                
                for i in range(4):
                    num = int(cur[i])
                    nxt = cur[:i] + str((num + 1) % 10) + cur[i+1:]
                    if nxt not in deadends:
                        deadends.add(nxt)
                        queue.append(nxt)
                    
                    nxt = cur[:i] + str((num - 1) % 10) + cur[i+1:]
                    if nxt not in deadends:
                        deadends.add(nxt)
                        queue.append(nxt)
            steps += 1
        
        return -1