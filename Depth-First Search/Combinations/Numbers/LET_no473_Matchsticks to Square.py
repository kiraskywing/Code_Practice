class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        matchsticks.sort(reverse=True)
        target = total // 4
        if matchsticks[0] > target:
            return False
        return self.dfs([target] * 4, 0, matchsticks)
    
    def dfs(self, targets, index, nums):
        if index == len(nums):
            return True
        
        used = set()
        for i, cur in enumerate(targets):
            if cur >= nums[index] and cur not in used:
                targets[i] -= nums[index]
                if self.dfs(targets, index + 1, nums):
                    return True
                targets[i] += nums[index]
                used.add(cur)
        
        return False