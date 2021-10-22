class Solution:
    def frequencySort(self, s: str) -> str:
        table = collections.Counter(s)
        sub = []
        for k, v in table.items():
            heapq.heappush(sub, (-v, k * v))
        
        res = ""
        while sub:
            _, string = heapq.heappop(sub)
            res += string
        return res