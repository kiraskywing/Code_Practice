class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        rec = [0] * 10
        count_a = count_b = 0
        
        for i in range(len(secret)):
            a = ord(secret[i]) - ord('0')
            b = ord(guess[i]) - ord('0')
            
            if a == b:
                count_a += 1
            else:
                if rec[a] < 0:
                    count_b += 1
                if rec[b] > 0:
                    count_b += 1
                rec[a] += 1
                rec[b] -= 1
        
        return f"{count_a}A{count_b}B"