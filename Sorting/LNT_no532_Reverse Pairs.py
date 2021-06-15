class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """

    def reversePairs(self, A):
        if len(A) < 2:
            return 0

        self.temp = [0 for _ in range(len(A))]
        self.count = 0
        self.merge_sorter(A, 0, len(A) - 1)
        return self.count

    def merge_sorter(self, A, left, right):
        if left >= right:
            return

        mid = (left + right) // 2
        self.merge_sorter(A, left, mid)
        self.merge_sorter(A, mid + 1, right)
        self.merger(A, left, right)

    def merger(self, A, left, right):

        mid = (left + right) // 2
        i, j = left, mid + 1
        index = left

        while i <= mid and j <= right:
            if A[i] > A[j]:
                self.temp[index] = A[j]
                j += 1
                self.count += mid - i + 1
            else:
                self.temp[index] = A[i]
                i += 1
            index += 1

        while i <= mid:
            self.temp[index] = A[i]
            i += 1
            index += 1
        while j <= right:
            self.temp[index] = A[j]
            j += 1
            index += 1

        for index2 in range(left, right + 1):
            A[index2] = self.temp[index2]