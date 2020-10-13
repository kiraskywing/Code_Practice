class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        result = 1
        factor = 1
        for i in range(len(A) - 1, -1, -1):
            count = 0
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    count +=1
            result += factor * count
            factor *= len(A)-i
        return result
