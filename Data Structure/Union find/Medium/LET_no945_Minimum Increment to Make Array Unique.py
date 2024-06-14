class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        memo = {}

        def find_spot(x):
            memo[x] = find_spot(memo[x] + 1) if x in memo else x
            return memo[x]

        return sum(find_spot(num) - num for num in nums)