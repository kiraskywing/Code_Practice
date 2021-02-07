class Solution:
    def check(self, nums: List[int]) -> bool:
        check, n = 0, len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                check += 1
            if check > 1:
                return False
        return True