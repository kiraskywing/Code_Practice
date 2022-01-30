class FreqStack:

    def __init__(self):
        self.freq = collections.defaultdict(int)
        self.stack = collections.defaultdict(list)
        self.maxF = 0

    def push(self, x: int) -> None:
        self.freq[x] += 1
        self.maxF = max(self.maxF, self.freq[x])
        self.stack[self.freq[x]].append(x)

    def pop(self) -> int:
        res = self.stack[self.maxF].pop()
        if not self.stack[self.maxF]:
            self.maxF -= 1
        self.freq[res] -= 1
        return res
            


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()