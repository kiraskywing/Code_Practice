class Solution:
    """
    @param num: Given the candidate Numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """

    def combinationSum2(self, num, target):

        num.sort()
        result, use = [], [0] * len(num)
        self.dfs(num, target, 0, use, 0, [], result)
        return result

    def dfs(self, num, target, start, use, value, temp, result):

        if value == target:
            result.append(temp[:])
            return

        for i in range(start, len(num)):
            if num[i] + value <= target and (i == 0 or num[i - 1] != num[i] or use[i - 1] == 1):
                temp.append(num[i])
                use[i] = 1
                self.dfs(num, target, i + 1, use, value + num[i], temp, result)
                temp.pop()
                use[i] = 0
