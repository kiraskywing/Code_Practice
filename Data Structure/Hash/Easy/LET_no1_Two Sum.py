class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return empty list? => no
        # notice that the same element cannot be used twice.
        
        # Approach:
        # use hashmap to record (key, value) pair -> key: num, value: index
        # if num is picked up, find out whether num - k is in hashmap
        
        memo = dict()    # Space: O(n)
        for i, num in enumerate(nums):    # Time: O(n)
            if target - num in memo:
                return [memo[target - num], i]
            memo[num] = i
        
        return []