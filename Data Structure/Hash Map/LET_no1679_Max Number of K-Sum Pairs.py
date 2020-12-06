class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        record = collections.defaultdict(int)
        count = 0
        
        for num in nums:
            if k - num in record and record[k - num] > 0:
                count += 1
                record[k - num] -= 1
            else:
                record[num] += 1
        
        return count