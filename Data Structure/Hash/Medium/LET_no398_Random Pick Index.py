class Solution:

    def __init__(self, nums: List[int]):
        self.memo = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.memo[num].append(i)

    def pick(self, target: int) -> int:
        n = len(self.memo[target])
        return self.memo[target][random.randint(0, n - 1)]

class Solution2:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        res = -1
        count = 0
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                rand = random.randint(1, count)
                if rand == count:
                    res = i
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)