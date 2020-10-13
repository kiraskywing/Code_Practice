class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """

    def kSumII(self, A, k, target):
        result = []
        self.dfs(A, 0, k, target, [], result)
        return result

    def dfs(self, A, start, k, target, temp, result):
        if k == 0:
            if target == 0:
                result.append(temp[:])
            return

        for i in range(start, len(A)):
            temp.append(A[i])
            self.dfs(A, i + 1, k - 1, target - A[i], temp, result)
            temp.pop()