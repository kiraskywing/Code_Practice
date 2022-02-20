class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        temp = []
        for i in range(26):
            if counts[i] > 0:
                heapq.heappush(temp, (-i, counts[i]))
        
        res = []
        while temp:
            i, n = heapq.heappop(temp)
            c = chr(ord('a') + (-i))
            if not res or res[-1][-1] != c:
                times = min(n, repeatLimit)
                res.append(c * times)
                n -= times
                if n > 0:
                    heapq.heappush(temp, (i, n))
            else:
                if not temp:
                    break
                i2, n2 = heapq.heappop(temp)
                c = chr(ord('a') + (-i2))
                res.append(c)
                n2 -= 1
                if n2 > 0:
                    heapq.heappush(temp, (i2, n2))
                heapq.heappush(temp, (i, n))
        
        return ''.join(res)