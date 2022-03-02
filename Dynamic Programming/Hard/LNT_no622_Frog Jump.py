# The same as LeetCode no403. Frog Jump

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo = {stone:set() for stone in stones}
        memo[stones[0]].add(0)
        
        for stone in stones:
            for k in memo[stone]:
                for step in range(k - 1, k + 2):
                    if step > 0 and stone + step in memo:
                        memo[stone + step].add(step)
        
        return len(memo[stones[-1]]) > 0