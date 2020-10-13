class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """

    def isMatch(self, s, p):
        return self.isMatch_helper(s, 0, p, 0, {})

    def isMatch_helper(self, source, i, pattern, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(source):
            return self.is_valid(pattern[j:])
        if j == len(pattern):
            return False

        if j + 1 < len(pattern) and pattern[j + 1] == "*":
            matched = self.match_char(source[i], pattern[j]) and self.isMatch_helper(source, i + 1, pattern, j,
                                                                                     memo) or self.isMatch_helper(
                source, i, pattern, j + 2, memo)
        else:
            matched = self.match_char(source[i], pattern[j]) and self.isMatch_helper(source, i + 1, pattern, j + 1,
                                                                                     memo)

        memo[(i, j)] = matched
        return matched

    def is_valid(self, pattern):
        if len(pattern) % 2 == 1:
            return False

        for i in range(len(pattern) // 2):
            if pattern[i * 2 + 1] != "*":
                return False

        return True

    def match_char(self, s, p):
        return s == p or p == "."
