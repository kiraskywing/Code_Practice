class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        record = collections.defaultdict(int)
        for i in range(10, len(s) + 1):
            record[s[i - 10 : i]] += 1
        return [key for key, value in record.items() if value > 1]