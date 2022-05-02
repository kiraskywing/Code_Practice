class Solution:
    def findPermutation(self, s: str) -> List[int]:
        stack, res = [], []
        for i in range(len(s)):
            stack.append(i + 1)
            if s[i] == 'I':
                while stack:
                    res.append(stack.pop())
        res.append(len(s) + 1)
        while stack:
            res.append(stack.pop())
        return res
        
        # res = []
        # for i in range(len(s)):
        #     if s[i] == 'I':
        #         res.extend(range(i + 1, len(res), -1))
        # res.extend(range(len(s) + 1, len(res), -1))
        # return res