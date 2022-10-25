class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)

class Solution2:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        m, n = len(word1), len(word2)
        i = j = 0
        i2 = j2 = 0
        
        while i < m and j < n:
            if word1[i][i2] != word2[j][j2]:
                return False
            i2 += 1
            j2 += 1
            
            if i2 == len(word1[i]):
                i += 1
                i2 = 0
            if j2 == len(word2[j]):
                j += 1
                j2 = 0
        
        return i == m and j == n