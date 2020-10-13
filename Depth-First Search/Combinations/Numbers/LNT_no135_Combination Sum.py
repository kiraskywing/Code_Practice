class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum(self, candidates, target):

        candidates = sorted(list(set(candidates)))
        result = []
        self.dfs(candidates, target, 0, [], result)
        return result

    def dfs(self, candidates, target, start, temp, result):

        if target < 0:
            return

        if target == 0:
            result.append(temp[:])
            return

        for i in range(start, len(candidates)):
            temp.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, temp, result)
            temp.pop()