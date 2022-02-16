# The same as LeetCode no44. Wildcard Matching

class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """

    def isMatch(self, s, p):
        return self.match_helper(s, 0, p, 0, {})

    def match_helper(self, source, i, pattern, j, memo):

        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(source):
            if j == len(pattern):
                return True
            else:
                return set(pattern[j:]) == set(["*"])

        if j == len(pattern):
            return False

        if pattern[j] != "*":
            matched = self.match_char(source[i], pattern[j]) and self.match_helper(source, i + 1, pattern, j + 1, memo)
        else:
            matched = self.match_helper(source, i + 1, pattern, j, memo) or self.match_helper(source, i, pattern, j + 1,
                                                                                              memo)

        memo[(i, j)] = matched
        return matched

    def match_char(self, s, p):
        return s == p or p == "?"