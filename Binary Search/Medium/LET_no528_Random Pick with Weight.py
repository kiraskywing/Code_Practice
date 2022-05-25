class Solution:

    def __init__(self, w: List[int]):
        self.nums = w
        self.pre_sum = [0]
        for num in w:
            self.pre_sum.append(self.pre_sum[-1] + num)

    def pickIndex(self) -> int:
        num = random.randint(1, self.pre_sum[-1])
        idx = bisect.bisect_left(self.pre_sum, num)
        return idx - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()