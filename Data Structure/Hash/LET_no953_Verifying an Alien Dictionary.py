class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {c : chr(ord('a') + i) for i, c in enumerate(order)}
        temp = []
        for w in words: temp.append(''.join([dic[c] for c in w]))
        return temp == sorted(temp)