class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """

    def findMissing2(self, n, str):
        used = [False for _ in range(n + 1)]
        return self.helper(n, str, 0, used)

    def helper(self, n, string, index, used):
        if index >= len(string):
            result = []
            for i in range(1, n + 1):
                if not used[i]:
                    result.append(i)
            return result[0] if len(result) == 1 else -1

        if string[index] == '0':
            return -1

        for j in range(2, 0, -1):
            num = int(string[index: index + j])
            if 1 <= num <= n and not used[num]:
                used[num] = True
                target = self.helper(n, string, index + j, used)
                if target != -1:
                    return target
                used[num] = False

        return -1
