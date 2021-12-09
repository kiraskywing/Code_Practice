class Solution1:
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            arr[start] = -arr[start]
            return arr[start] == 0 or self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])
        return False

class Solution2:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = collections.deque([start])
        n = len(arr)
        while queue:
            cur = queue.popleft()
            if arr[cur] == 0:
                return True
            for i in [1, -1]:
                nxt = cur + i * arr[cur]
                if 0 <= nxt < n and arr[nxt] >= 0:
                    arr[nxt] = -arr[nxt]
                    queue.append(nxt)
        return False