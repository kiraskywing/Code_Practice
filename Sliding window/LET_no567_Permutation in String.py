class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        memo = collections.defaultdict(int)
        n, m = len(s1), len(s2)
        if n > m:
            return False
        for i in range(n):
            memo[s1[i]] += 1
            memo[s2[i]] -= 1
        if all(val == 0 for key, val in memo.items()):
            return True
        
        for i in range(n, m):
            memo[s2[i]] -= 1
            memo[s2[i - n]] += 1
            if all(val == 0 for key, val in memo.items()):
                return True
        
        return False