class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        memo = collections.defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                memo[i + j].append(nums[i][j])
                
        res = []
        for values in memo.values():
            res.extend(reversed(values))
        
        return res

"""
Given a 2D integer array nums, return all elements of nums in diagonal order.

Example 1:
Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]

| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |

Example 2:
Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

| 1 | 2 | 3 | 4 | 5 |
---------------------
| 6 | 7 |
---------------------
| 8 |
---------------------
| 9 | 10| 11|
---------------------
| 12| 13| 14| 15| 16|

"""