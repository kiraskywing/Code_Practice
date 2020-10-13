class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """

    def permutationIndexII(self, A):
        if not A:
            return 0

        index, factor, multi_factor = 1, 1, 1
        multi_count = collections.defaultdict(int)

        for i in range(len(A) - 1, -1, -1):
            multi_count[A[i]] += 1
            multi_factor *= multi_count[A[i]]

            count = 0
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    count += 1
            index += count * factor // multi_factor
            factor *= (len(A) - i)

        return index
