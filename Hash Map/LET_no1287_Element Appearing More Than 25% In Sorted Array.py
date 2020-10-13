class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        target = len(arr) / 4
        memo = collections.defaultdict(int)
        for num in arr:
            memo[num] += 1
            if memo[num] > target:
                return num