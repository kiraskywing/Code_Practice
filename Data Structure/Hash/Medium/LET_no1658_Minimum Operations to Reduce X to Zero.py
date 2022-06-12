class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        record = {0 : 0}
        prefix = 0
        for i, num in enumerate(nums, 1):
            prefix += num
            record[prefix] = i
            
        res = record[x] if x in record else float('inf')
        
        for i, num in enumerate(reversed(nums), 1):
            x -= num
            if x in record and record[x] + i <= len(nums):
                res = min(res, record[x] + i)
        
        return res if res != float('inf') else -1