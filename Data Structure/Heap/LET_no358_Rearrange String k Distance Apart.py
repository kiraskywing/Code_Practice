class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        
        memo = collections.Counter(s)
        size = len(s)
        pq = []
        for c, val in memo.items():
            heapq.heappush(pq, (-val, c))

        res = []
        while pq:
            times = min(k, size)
            temp = []
            for _ in range(times):
                if not pq:
                    return ""
                val, c = heapq.heappop(pq)
                res.append(c)
                size -= 1
                val += 1
                if val < 0:
                    temp.append((val, c))
            
            for val, c in temp:
                heapq.heappush(pq, (val, c))

        return ''.join(res)
