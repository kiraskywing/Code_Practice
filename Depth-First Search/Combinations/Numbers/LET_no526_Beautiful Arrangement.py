class Solution:
    def countArrangement(self, n: int) -> int:
        return self.helper(n, set(range(1, n + 1)))
    
    def helper(self, i, nums_to_use):
        if i == 1:
            return 1
        return sum(self.helper(i - 1, nums_to_use - {x}) for x in nums_to_use if x % i == 0 or i % x == 0)