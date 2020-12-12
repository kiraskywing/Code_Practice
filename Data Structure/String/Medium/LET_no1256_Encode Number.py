class Solution:
    def encode(self, num: int) -> str:
        return self.encode((num - 1) // 2) + "10"[num % 2] if num else ""

        """
        if num == 0:
            return ""

        count = 0
        temp = num + 1
        while temp > 1:
            count += 1; temp //= 2

        result = ["0"] * count

        temp = num - (2 ** count - 1)
        i = count
        while i > -1:
            if temp >= 2 ** i:
                result[-(i + 1)] = "1"
                temp -= 2 ** i
            i -= 1

        return ''.join(result)
        """