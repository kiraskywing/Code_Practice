class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        record = collections.defaultdict(int)
        for num in nums:
            record[num] += 1
        ans = 0
        for num in record:
            if k == 0 and record[num] > 1:
                ans += 1
            if k > 0 and num + k in record:
                ans += 1
        return ans