class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        i = 1
        count = 0
        while i <= 10000000:
            cur = 0
            for num in candidates:
                if num & i:
                    cur += 1
            count = max(count, cur)
            i <<= 1
        return count