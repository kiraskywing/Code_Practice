class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        n = 0
        for i, c in enumerate(S):
            n = n * int(c) if  c.isdigit() else n + 1
            if n >= K:
                break
        for j in range(i, -1, -1):
            c = S[j]
            if c.isdigit():
                n //= int(c)
                K %= n
            else:
                if K == n or K == 0:
                    return c
                n -= 1