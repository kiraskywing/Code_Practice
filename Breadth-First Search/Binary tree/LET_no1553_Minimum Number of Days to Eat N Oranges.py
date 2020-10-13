class Solution:
    def minDays(self, n: int) -> int:
        ans = 0
        queue = collections.deque([n])
        seen = set()
        
        while queue:
            for _ in range(len(queue)):
                num = queue.popleft()
                if num == 0:
                    return ans
                seen.add(num)
                if num - 1 not in seen:
                    queue.append(num - 1)
                if num % 2 == 0 and num // 2 not in seen:
                    queue.append(num // 2)
                if num % 3 == 0 and num // 3 not in seen:
                    queue.append(num // 3)
            ans += 1