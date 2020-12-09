class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        record = collections.defaultdict(int)
        res = 0
        for cur in time:
            cur %= 60
            res += record[(60 - cur) % 60]
            record[cur] += 1
            
        return res