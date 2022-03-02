# The same as LeetCode no45. Jump Game II

class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """

    def jump(self, A):
        """
        Greedy
        """
        cur_end = farthest = jumps = 0
        for i in range(len(A) - 1):
            farthest = max(farthest, i + A[i])
            if i == cur_end:
                jumps += 1
                cur_end = farthest
        
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
