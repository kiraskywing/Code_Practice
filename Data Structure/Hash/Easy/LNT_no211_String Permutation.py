class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """

    def Permutation(self, A, B):
        if len(A) != len(B):
            return False

        count = collections.defaultdict(int)
        for c in A:
            count[c] += 1
        for c in B:
            count[c] -= 1
        for c in count:
            if count[c] != 0:
                return False
        return True
