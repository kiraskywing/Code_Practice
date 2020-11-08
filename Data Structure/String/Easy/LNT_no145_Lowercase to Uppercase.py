class Solution:
    """
    @param character: a character
    @return: a character
    """

    def lowercaseToUppercase(self, character):
        """
        return character.upper()
        """

        return chr(ord("A") + (ord(character) - ord("a")))