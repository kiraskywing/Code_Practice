class Solution:
    def checkValidString(self, s: str) -> bool:
        lefts, rights, wilds = [], [], []
        for i, c in enumerate(s):
            if c == '(':
                lefts.append(i)
            elif c == ')':
                if lefts:
                    lefts.pop()
                elif wilds:
                    wilds.pop()
                else:
                    rights.append(i)
            else:
                wilds.append(i)

        while lefts and wilds and lefts[-1] < wilds[-1]:
            lefts.pop()
            wilds.pop()

        return not lefts and not rights