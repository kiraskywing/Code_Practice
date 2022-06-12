class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        memo = collections.defaultdict(set)
        for s in ideas:
            memo[s[0]].add(s[1:])
            
        temp = [val for val in memo.values()]
        res = 0
        for i in range(len(temp) - 1):
            for j in range(i + 1, len(temp)):
                inter = temp[i] & temp[j]
                res += len(temp[i] - inter) * len(temp[j] - inter) * 2
        return res