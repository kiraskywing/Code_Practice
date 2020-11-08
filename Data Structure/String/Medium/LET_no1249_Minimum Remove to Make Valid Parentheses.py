class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        removes = set()
        unpatch = 0
        lefts = []

        for i, char in enumerate(s):
            if char == "(":
                unpatch += 1
                lefts.append(i)

            elif char == ")":
                unpatch -= 1

                if unpatch < 0:
                    removes.add(i)
                    unpatch = 0
                else:
                    lefts.pop()

        for i in lefts:
            removes.add(i)

        return ''.join(char for i, char in enumerate(s) if i not in removes)