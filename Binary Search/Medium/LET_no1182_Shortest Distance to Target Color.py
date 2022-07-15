class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        memo = collections.defaultdict(list)
        for i, color in enumerate(colors):
            memo[color].append(i)
            
        res = []
        for i, color in queries:
            n = len(memo[color])
            if n == 0:
                res.append(-1)
            else:
                j = bisect.bisect(memo[color], i)
                idx = memo[color][min(j, n - 1)]
                idx2 = memo[color][max(j - 1, 0)]
                res.append(min(abs(i - idx), abs(i - idx2)))
        
        return res