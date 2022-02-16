# The same as LeetCode no40. Combination Sum II

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
    
    def dfs(self, nums, target, start, temp, res):
        if target < 0:
            return
        if target == 0:
            res.append(temp[:])
            return
        
        for i in range(start, len(nums)):
            if i != start and nums[i] == nums[i - 1]:
                continue
            temp.append(nums[i])
            self.dfs(nums, target - nums[i], i + 1, temp, res)
            temp.pop()