class Solution:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """

    def stringReplace(self, a, b, s):

        seed = 33
        mod = 1000000007
        max_len = -1
        a_hash, s_hash, order = [], [], []

        for string in a:
            key = 1
            max_len = max(max_len, len(string))
            for ch in string:
                key = (key * seed + ord(ch) - ord('a')) % mod
            a_hash.append(key)

        key = 1
        s_hash.append(key)
        max_len = max(max_len, len(s))
        for ch in s:
            key = (key * seed + ord(ch) - ord('a')) % mod
            s_hash.append(key)

        key = 1
        order.append(key)
        for i in range(max_len):
            key = key * seed % mod
            order.append(key)

        result = [ch for ch in s]
        i = 0
        while i < len(s):
            max_len, index = -1, 0
            for j in range(len(a)):
                len_a = len(a[j])
                left, right = i + 1, i + len_a
                if right > len(s):
                    continue
                s_hash_value = (s_hash[right] - s_hash[left - 1] * order[right - left + 1] % mod + mod) % mod
                a_hash_value = (a_hash[j] - order[len_a] + mod) % mod
                if s_hash_value == a_hash_value and len_a > max_len:
                    max_len = len_a
                    index = j

            if max_len != -1:
                for k in range(max_len):
                    result[i + k] = b[index][k]
                i += (max_len - 1)

            i += 1

        return ''.join(result)
