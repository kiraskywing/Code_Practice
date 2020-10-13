class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers2(self, A):
        self.temp = [0 for _ in range(len(A))]
        self.sorter(A, 0, len(A) - 1)

    def sorter(self, A, left, right):
        if left >= right:
            return

        mid = (left + right) // 2
        self.sorter(A, left, mid)
        self.sorter(A, mid + 1, right)
        self.merger(A, left, right)

    def merger(self, A, left, right):

        mid = (left + right) // 2
        i, j = left, mid + 1
        index = left

        while i <= mid and j <= right:
            if A[i] <= A[j]:
                self.temp[index] = A[i]
                i += 1
            else:
                self.temp[index] = A[j]
                j += 1
            index += 1

        while i <= mid:
            self.temp[index] = A[i]
            i += 1
            index += 1
        while j <= right:
            self.temp[index] = A[j]
            j += 1
            index += 1

        for k in range(left, right + 1):
            A[k] = self.temp[k]

        """
        n = right - left + 1
        mid = (left + right) // 2
        i, j = left, mid + 1

        for k in range(n):

            if i <= mid and (j > right or A[i] <= A[j]):
                self.temp[k] = A[i]
                i += 1

            else:
                self.temp[k] = A[j]
                j += 1

        for k in range(n):
            A[left + k] = self.temp[k]
        """
