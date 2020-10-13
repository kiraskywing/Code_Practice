class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """

    def firstUniqChar(self, str):
        counter = collections.defaultdict(int)

        for c in str:
            counter[c] += 1

        for c in str:
            if counter[c] == 1:
                return c
