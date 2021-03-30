class Solution:
    def originalDigits(self, s: str) -> str:
        res = []
        words = ["zero", "two", "four", "six", "eight", "one", "three", "five", "seven", "nine"]
        nums = ["0", "2", "4", "6", "8", "1", "3", "5", "7", "9"]
        s = collections.Counter(s)
        
        for word, num in zip(words, nums):
            word = collections.Counter(word)
            count = min(s[c] // word[c] for c in word)
            if count == 0: continue
            res.append(num * count)
            for c in word: s[c] -= word[c] * count
        
        return ''.join(sorted(res))