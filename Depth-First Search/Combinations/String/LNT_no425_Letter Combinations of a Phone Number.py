# The same as LeetCode no17. Letter Combinations of a Phone Number

KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits):

        if not digits:
            return []

        result = []
        self.dfs(digits, 0, [], result)
        return result

    def dfs(self, digits, index, string, result):

        if index == len(digits):
            result.append(''.join(string))
            return

        for letter in KEYBOARD[digits[index]]:
            string.append(letter)
            self.dfs(digits, index + 1, string, result)
            string.pop()
