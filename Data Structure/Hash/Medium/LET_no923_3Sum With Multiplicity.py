class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        record = collections.Counter(arr)
        res = 0
        for i in record:
            for j in record:
                k = target - i - j
                if i == j == k:
                    res += record[i] * (record[i] - 1) * (record[i] - 2) // 6
                elif i == j != k:
                    res += record[i] * (record[i] - 1) // 2 * record[k]
                elif i < j and j < k:
                    res += record[i] * record[j] * record[k]
        
        return res % (10 ** 9 + 7)