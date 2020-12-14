class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        base, mod = 33, 1000000007
        result = set()
        n = len(text)
        hashmap = [0] * (n + 1)
        power = [0] * (n + 1)
        hashmap[0], power[0] = 1, 1

        for i in range(1, n + 1):
            hashmap[i] = (hashmap[i - 1] * base + ord(text[i - 1])) % mod
            power[i] = power[i - 1] * base % mod

        for i in range(n):
            for j in range(i + 2, n + 1, 2):
                mid = (i + j) // 2
                key1 = self.get_hash(i, mid, hashmap, power, mod)
                key2 = self.get_hash(mid, j, hashmap, power, mod)
                if key1 == key2:
                    result.add(key1)

        return len(result)

    def get_hash(self, left, right, hashmap, power, mod):
        return (hashmap[right] - hashmap[left] * power[right - left] % mod + mod) % mod
