class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def countOfSmallerNumberII(self, A):
        if not A:
            return []

        root = SegTree(0, max(A))
        result = []
        for num in A:
            result.append(root.sum(0, num - 1))
            root.index_count(num)
        return result


class SegTree:

    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
        self.count = 0

        if start != end:
            self.left = SegTree(start, (start + end) // 2)
            self.right = SegTree((start + end) // 2 + 1, end)

    def sum(self, start, end):
        if start <= self.start and self.end <= end:
            return self.count

        if self.start == self.end:
            return 0

        if end <= self.left.end:
            return self.left.sum(start, end)
        if start >= self.right.start:
            return self.right.sum(start, end)

        return self.left.sum(start, self.left.end) + self.right.sum(self.right.start, end)

    def index_count(self, index):
        if self.start == self.end:
            self.count += 1
            return

        if index <= self.left.end:
            self.left.index_count(index)
        else:
            self.right.index_count(index)

        self.count = self.left.count + self.right.count
