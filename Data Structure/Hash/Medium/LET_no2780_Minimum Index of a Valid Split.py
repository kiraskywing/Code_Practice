class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        left = collections.defaultdict(int)
        right = collections.Counter(nums)
        n = len(nums)
        
        for i in range(n):
            left[nums[i]] += 1
            right[nums[i]] -= 1

            if left[nums[i]] * 2 > i + 1 and right[nums[i]] * 2 > n - i - 1:
                return i

        return -1
    