class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        memo = collections.Counter(arr)
        return len(memo) == len(set(memo.values()))