# The same as LeetCode no27. Remove Element

class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """

    def removeElement(self, A, elem):
        if not A:
            return 0

        index = 0
        for i in range(len(A)):
            if A[i] != elem:
                A[index] = A[i]
                index += 1
        return index