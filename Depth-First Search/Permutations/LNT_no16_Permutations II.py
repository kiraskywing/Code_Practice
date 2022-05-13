# The same as Leetcode no47_Permutations II

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        self.dfs(collections.Counter(nums), n, [], res)
        return res
    
    def dfs(self, memo, n, temp, res):
        if len(temp) == n:
            res.append(temp[:])
            return
        
        for num in memo:
            if memo[num] > 0:
                 memo[num] -= 1
                 temp.append(num)
                 self.dfs(memo, n, temp, res)
                 temp.pop()
                 memo[num] += 1
            