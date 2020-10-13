class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        memo = collections.defaultdict(int)
        result = 0

        for i in range(len(s) - minSize + 1):
            temp = s[i: i + minSize]
            if len(set(temp)) <= maxLetters:
                memo[temp] += 1
                result = max(result, memo[temp])
        return result