# The same as LeetCode no291. Word Pattern II

class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """

    def wordPatternMatch(self, pattern, str):
        return self.is_match(pattern, str, {}, set())

    def is_match(self, pattern, string, mapping, used):
        if len(pattern) == 0:
            return len(string) == 0

        char = pattern[0]
        if char in mapping:
            word = mapping[char]
            if not string.startswith(word):
                return False
            return self.is_match(pattern[1:], string[len(word):], mapping, used)

        for i in range(len(string)):
            word = string[: i + 1]
            if word in used:
                continue

            used.add(word)
            mapping[char] = word

            if self.is_match(pattern[1:], string[i + 1:], mapping, used):
                return True

            del mapping[char]
            used.remove(word)

        return False