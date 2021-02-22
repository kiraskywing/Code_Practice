class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        numIndex = groupIndex = 0
        while groupIndex < len(groups) and numIndex < len(nums):
            matchCount = 0
            while numIndex + matchCount < len(nums) and matchCount < len(groups[groupIndex]) and groups[groupIndex][matchCount] == nums[numIndex + matchCount]:
                matchCount += 1
            
            if matchCount == len(groups[groupIndex]):
                groupIndex += 1
                numIndex += matchCount
            else:
                numIndex += 1
        
        return groupIndex == len(groups)