class Solution:
    """
    @param names: a string array
    @return: a string array
    """
    def nameDeduplication(self, names):

        note = set()

        for item in names:
            item = item.lower()
            if item not in note:
                note.add(item)

        return list(note)