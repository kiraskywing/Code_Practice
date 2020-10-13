class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):

        for i in range(len(A)):
            index_min = i

            for j in range(i + 1, len(A)):
                if A[j] <= A[index_min]:
                    index_min = j

            A[i], A[index_min] = A[index_min], A[i]