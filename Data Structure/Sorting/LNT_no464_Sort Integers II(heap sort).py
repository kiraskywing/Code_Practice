class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):

        self.bulid_maxheap(A)
        size = len(A)

        for i in range(len(A) - 1, 0, -1):
            A[0], A[i] = A[i], A[0]
            size -= 1
            self.maxheapify(A, 0, size)

    def bulid_maxheap(self, A):

        for i in range(len(A) // 2 - 1, -1, -1):
            self.maxheapify(A, i, len(A))

    def maxheapify(self, A, i, size):

        root = i
        while True:
            child = root * 2 + 1
            if child >= size:
                break
            if child + 1 < size and A[child] < A[child + 1]:
                child += 1
            if A[root] < A[child]:
                A[root], A[child] = A[child], A[root]
                root = child
            else:
                break

        """
        left = i * 2 + 1
        right = i * 2 + 2

        if left < size and A[left] > A[i]:
            largest = left
        else:
            largest = i

        if right < size and A[right] > A[largest]:
            largest = right

        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.maxheapify(A, largest, size)
        """