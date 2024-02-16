class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        memo = list(collections.Counter(arr).values())
        memo.sort()
        n = len(memo)
        for counts in memo:
            cur = min(counts, k)
            counts -= cur
            k -= cur
            n -= counts == 0
            if k == 0:
                return n
        
        return n