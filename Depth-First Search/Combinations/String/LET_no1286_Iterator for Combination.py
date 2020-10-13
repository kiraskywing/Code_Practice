class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.memo = []
        self.dfs([], characters, combinationLength)
        self.count = 0

    def next(self) -> str:
        self.count += 1
        return self.memo[self.count - 1]

    def hasNext(self) -> bool:
        return self.count < len(self.memo)

    def dfs(self, path, chars, length):
        if length == 0:
            self.memo.append(''.join(path))
            return

        for i in range(len(chars)):
            if i + 1 <= len(chars):
                path.append(chars[i])
                self.dfs(path, chars[i + 1:], length - 1)
                path.pop()

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()