class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        temp = []
        for t1, t2 in flowers:
            temp.append((t1, 1))
            temp.append((t2 + 1, -1))
        
        temp.sort()
        i, m = 0, len(temp)
        memo = collections.defaultdict(int)
        cur = 0
        while i < m:
            t = temp[i][0]
            cur += temp[i][1]
            i += 1
            while i < m and temp[i][0] == t:
                cur += temp[i][1]
                i += 1
            memo[t] = cur
        
        times = [0] + [t for t in sorted(memo)]
        res = []
        for t in persons:
            i = bisect.bisect(times, t)
            res.append(memo[times[i - 1]])
        return res