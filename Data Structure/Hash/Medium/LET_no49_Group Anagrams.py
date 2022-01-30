class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record = collections.defaultdict(list)
        for s in strs:
            record[self.bucketSort(s)].append(s)
        
        return [lst for lst in record.values()]
        
    def bucketSort(self, s):
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        res = []
        for i in range(26):
            res.append(chr(ord('a') + i) * counts[i])
        return ''.join(res)