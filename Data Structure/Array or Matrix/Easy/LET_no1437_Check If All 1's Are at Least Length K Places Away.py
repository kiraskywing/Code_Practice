class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = None
        for i, n in enumerate(nums):
            if n == 1:
                if prev is not None and i - prev - 1 < k:
                    return False
                prev = i
        return True