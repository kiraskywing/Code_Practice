class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, 0, [], res)
        return res
    
    def helper(self, nums, start, temp, res):
        if len(temp) > 1:
            res.append(temp[:])
            
        visited = set()
        for i in range(start, len(nums)):
            if (not temp or nums[i] >= temp[-1]) and nums[i] not in visited:
                visited.add(nums[i])
                temp.append(nums[i])
                self.helper(nums, i + 1, temp, res)
                temp.pop()