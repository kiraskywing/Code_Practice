class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """

    def jump(self, A):
        """
        Greedy
        """
        start, end, jumps = 0, 0, 0

        while end < len(A) - 1:
            jumps += 1
            farthest = end
            for i in range(start, end + 1):
                farthest = max(farthest, A[i] + i)

            start = end + 1
            end = farthest

        return jumps

        """
        O(n^2) solution

        steps = [sys.maxsize for _ in range(len(A))]
        steps[0] = 0

        for i in range(1, len(A)):
            for j in range(0, i):
                if steps[j] != sys.maxsize and j + A[j] >= i:
                    steps[i] = min(steps[i], steps[j] + 1)

        return steps[-1]
        """
