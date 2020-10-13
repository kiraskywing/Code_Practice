class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """

    def partition(self, s):

        result = []
        self.dfs(result, [], s)
        return result

    def dfs(self, result, path, string):

        if len(string) == 0:
            result.append(path[:])
            return

        for i in range(1, len(string) + 1):
            if self.is_palindrome(string[:i]):
                path.append(string[:i])
                self.dfs(result, path, string[i:])
                path.pop()

    def is_palindrome(self, string):
        return string == string[::-1]