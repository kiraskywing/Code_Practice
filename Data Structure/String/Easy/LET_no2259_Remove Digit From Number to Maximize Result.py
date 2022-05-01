class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        for i in range(len(number) - 1):
            if number[i] == digit and number[i + 1] > number[i]:
                return number[:i] + number[i + 1:]
        
        i = len(number) - 1
        while i >= 0 and number[i] != digit:
            i -= 1
        return number[:i] + number[i + 1:]