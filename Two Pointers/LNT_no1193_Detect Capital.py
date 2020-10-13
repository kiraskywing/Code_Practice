class Solution:
    """
    @param word: a string
    @return: return a boolean
    """

    def detectCapitalUse(self, word):
        if "A" <= word[0] <= "Z" and "A" <= word[-1] <= "Z":
            for i in range(1, len(word) - 1):
                if not ("A" <= word[i] <= "Z"):
                    return False
            return True

        elif "A" <= word[0] <= "Z":
            for i in range(1, len(word)):
                if not ("a" <= word[i] <= "z"):
                    return False
            return True

        else:
            for i in range(1, len(word)):
                if not ("a" <= word[i] <= "z"):
                    return False
            return True
