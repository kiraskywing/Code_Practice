class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.count = 0

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        res = 0
        root = Node()
        for i in range(len(nums)):
            res += self.insert(root, nums, i, k, p)
        return res
        
    def insert(self, cur, nums, i, k, p):
        if i == len(nums):
            return 0
        k -= int(nums[i] % p == 0)
        if k < 0:
            return 0
        
        cur.children[nums[i]].count += 1
        return int(cur.children[nums[i]].count == 1) + self.insert(cur.children[nums[i]], nums, i + 1, k, p)