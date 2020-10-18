class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        queue, seen, result = collections.deque([s]), {s}, s
        
        while queue:
            cur = queue.popleft()
            result = min(result, cur)
            
            func_add = list(cur)
            for i, ch in enumerate(func_add):
                if i % 2 != 0: func_add[i] = str((int(ch) + a) % 10)
            func_add = ''.join(func_add)
            if func_add not in seen:
                seen.add(func_add)
                queue.append(func_add)
            
            func_rotate = cur[-b:] + cur[:-b]
            if func_rotate not in seen:
                seen.add(func_rotate)
                queue.append(func_rotate)
        
        return result