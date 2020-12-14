class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word in words)

        result = []
        for i in range(max_len):
            temp = []
            for word in words:
                if i < len(word):
                    temp.append(word[i])
                else:
                    temp.append(' ')
            result.append(''.join(temp).rstrip())

        return result