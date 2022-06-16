class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """

    def restoreIpAddresses(self, s):
        result = []
        self.dfs(s, 0, result, [])
        return result

    def dfs(self, string, count, result, temp):
        if count == 4:
            if string == '':
                result.append('.'.join(temp))
            return

        for i in range(1, 4):
            if i <= len(string) and int(string[:i]) <= 255:
                temp.append(string[:i])
                self.dfs(string[i:], count + 1, result, temp)
                temp.pop()
                if string[0] == '0':
                    break
