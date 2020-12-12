class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        seen = [0, 0, 0]

        for num in nums:
            for i in seen[:]:
                seen[(num + i) % 3] = max(seen[(num + i) % 3], num + i)

        return seen[0]