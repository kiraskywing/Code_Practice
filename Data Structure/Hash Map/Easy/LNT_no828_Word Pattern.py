# The same as LeetCode no290. Word Pattern

class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """

    def wordPattern(self, pattern, teststr):

        memo = dict()
        used = set()
        str_list = teststr.split()

        if len(pattern) != len(str_list):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in memo:
                if str_list[i] not in used:
                    memo[pattern[i]] = str_list[i]
                    used.add(str_list[i])
                else:
                    return False

            if memo[pattern[i]] != str_list[i]:
                return False

        return True
